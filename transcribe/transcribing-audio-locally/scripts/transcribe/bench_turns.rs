mod support;

use std::collections::BTreeSet;
use std::path::Path;
use std::time::Instant;

use speakrs::{ExecutionMode, OwnedDiarizationPipeline};

use support::{ExampleResult, load_wav_samples};

fn main() -> ExampleResult<()> {
    support::init_tracing();
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: cargo run --release --example bench_turns --features coreml -- <audio.wav>");
        std::process::exit(1);
    }
    let audio_path = Path::new(&args[1]);

    let audio = load_wav_samples(audio_path)?;
    let duration_s = audio.len() as f64 / 16_000.0;

    let t_load = Instant::now();
    let mut pipeline = OwnedDiarizationPipeline::from_pretrained(ExecutionMode::CoreMl)?;
    let load_s = t_load.elapsed().as_secs_f64();

    // warmup-then-measure would need two passes; we do a single cold+warm split:
    let t_run = Instant::now();
    let result = pipeline.run(&audio)?;
    let run_s = t_run.elapsed().as_secs_f64();

    let segments = result.discrete_diarization.to_segments();
    let speakers: BTreeSet<String> = segments.iter().map(|s| s.speaker.clone()).collect();

    // write turns to stdout (redirected to file by caller)
    for segment in &segments {
        println!("{:.3}\t{:.3}\t{}", segment.start, segment.end, segment.speaker);
    }

    eprintln!("=== SPEAKRS BENCH ===");
    eprintln!("audio_duration_s: {duration_s:.1}");
    eprintln!("model_load_s:     {load_s:.2}");
    eprintln!("diarize_run_s:    {run_s:.2}");
    eprintln!("realtime_factor:  {:.1}x", duration_s / run_s);
    eprintln!("num_speakers:     {}", speakers.len());
    eprintln!("num_turns:        {}", segments.len());
    Ok(())
}
