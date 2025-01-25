# Graphical Interface Documentation

## Introduction

This document provides instructions for installing and running the graphical interface for the audio analysis and resynthesis application built on top of loristrck. The graphical interface is implemented using PyQt5 and provides an intuitive way to load, analyze, and manipulate audio files.

## Installation

To install the graphical interface, follow these steps:

1. Ensure you have Python 3.9 or higher installed on your system.
2. Install the required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file should include the following dependencies:
   ```
   numpy
   PyQt5
   matplotlib
   scipy
   soundfile
   ```

## Running the Application

To run the graphical interface, execute the following command:
```bash
python -m loristrck.gui
```

## Features and Functionalities

### Loading Audio Files

The graphical interface allows you to load audio files in various formats, such as WAV, AIFF, and SDIF. To load an audio file, click on the "Load Audio File" button and select the desired file from your file system.

### Visualizing Sounds

The application provides multiple representations of the loaded audio file, including waveform, spectrogram, and partial tracking displays. These visualizations help you understand the spectral content of the audio file and make informed decisions about processing and transformations.

### Fine-Tuning Analysis Parameters

You can fine-tune the analysis parameters, such as resolution, window size, and frequency drift, using the provided sliders and input fields. The changes are applied in real-time, allowing you to see the effects of your adjustments immediately.

### Custom Rules and Transformations

The application integrates numpy for creating custom rules and transformations. You can apply time-stretching, frequency shifting, and harmonic remapping to the analyzed partials. Additionally, you can define amplitude-dependent transformations and snap frequencies to specific musical scales or chord structures.

### Real-Time Playback and Export

The graphical interface supports real-time playback of the processed sounds. You can also export the modified partials as high-quality resynthesized audio files or save the analysis data for further processing.

## Examples and Usage Scenarios

### Example 1: Basic Analysis and Visualization

1. Load an audio file by clicking on the "Load Audio File" button.
2. Adjust the analysis resolution using the slider.
3. Observe the waveform, spectrogram, and partial tracking displays to understand the spectral content of the audio file.

### Example 2: Applying Time-Stretching

1. Load an audio file by clicking on the "Load Audio File" button.
2. Adjust the analysis resolution using the slider.
3. Apply time-stretching by selecting the desired factor from the transformation options.
4. Observe the changes in the partial tracking display and listen to the real-time playback.

### Example 3: Frequency Shifting and Harmonic Remapping

1. Load an audio file by clicking on the "Load Audio File" button.
2. Adjust the analysis resolution using the slider.
3. Apply frequency shifting by selecting the desired shift value from the transformation options.
4. Apply harmonic remapping by selecting the desired mapping from the transformation options.
5. Observe the changes in the partial tracking display and listen to the real-time playback.

### Example 4: Exporting Processed Audio

1. Load an audio file by clicking on the "Load Audio File" button.
2. Adjust the analysis resolution using the slider.
3. Apply the desired transformations (e.g., time-stretching, frequency shifting, harmonic remapping).
4. Click on the "Save" button to export the processed audio file.
5. Select the desired file format and location to save the file.

## Conclusion

The graphical interface for the audio analysis and resynthesis application built on top of loristrck provides an intuitive and powerful tool for musicians, sound designers, and researchers. By combining advanced spectral analysis techniques with numpy's mathematical flexibility, the application enables users to perform complex audio manipulations with ease.
