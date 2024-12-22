import cv2
import numpy as np
import time
from datetime import datetime
import os

class TenetRecorder:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("Could not open camera")
        self.frames = []
        self.output_dir = "tenet_recordings"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
            
    def record_original(self, duration=10):
        """Record original footage"""
        start_time = time.time()
        print("Recording original footage...")
        while time.time() - start_time < duration:
            ret, frame = self.cap.read()
            if ret:
                self.frames.append(frame.copy())
                # Add recording indicator
                cv2.circle(frame, (30, 30), 10, (0, 0, 255), -1)
                cv2.putText(frame, "RECORDING", (50, 40), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.imshow('Tenet Recording', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyWindow('Tenet Recording')
        
    def create_inverted_sequence(self):
        """Create and save both normal and inverted sequences"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Set up video writers
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        frame_size = (int(self.cap.get(3)), int(self.cap.get(4)))
        fps = 30
        
        # Original sequence
        original_file = os.path.join(self.output_dir, f'original_{timestamp}.avi')
        original_writer = cv2.VideoWriter(original_file, fourcc, fps, frame_size)
        
        # Inverted sequence
        inverted_file = os.path.join(self.output_dir, f'inverted_{timestamp}.avi')
        inverted_writer = cv2.VideoWriter(inverted_file, fourcc, fps, frame_size)
        
        # Save original sequence
        print("Saving original sequence...")
        for frame in self.frames:
            original_writer.write(frame)
            
        # Create and save inverted sequence
        print("Creating and saving inverted sequence...")
        for frame in reversed(self.frames):
            inverted_writer.write(frame)
            cv2.imshow('Inverted Playback', frame)
            cv2.waitKey(33)  # ~30fps playback
            
        # Clean up
        original_writer.release()
        inverted_writer.release()
        cv2.destroyAllWindows()
        
        return original_file, inverted_file
        
    def run_full_sequence(self):
        """Run the complete recording and inversion process"""
        try:
            # Step 1: Record original footage
            self.record_original()
            
            if len(self.frames) == 0:
                print("No frames were recorded!")
                return
                
            # Step 2: Create and save sequences
            original_file, inverted_file = self.create_inverted_sequence()
            print(f"\nRecording complete!")
            print(f"Original footage saved as: {original_file}")
            print(f"Inverted footage saved as: {inverted_file}")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            self.cap.release()
            cv2.destroyAllWindows()
            
    def __del__(self):
        """Cleanup when object is destroyed"""
        if self.cap.isOpened():
            self.cap.release()

if __name__ == "__main__":
    print("Tenet-Style Temporal Inversion Recorder")
    print("--------------------------------------")
    print("Press 'Q' to stop recording early")
    print("Starting in 3 seconds...")
    time.sleep(3)
    
    recorder = TenetRecorder()
    recorder.run_full_sequence()