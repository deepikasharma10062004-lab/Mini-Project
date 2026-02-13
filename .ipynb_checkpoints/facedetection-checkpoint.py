{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "636054b6-4aea-44b9-9571-c3084129dbdc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "# Load Haar Cascade file\n",
    "face_cap = cv2.CascadeClassifier(\n",
    "    cv2.data.haarcascades + \"haarcascade_frontalface_default.xml\"\n",
    ")\n",
    "\n",
    "# Open webcam\n",
    "video_cap = cv2.VideoCapture(0)\n",
    "\n",
    "while True:\n",
    "    ret, video_data = video_cap.read()\n",
    "    if not ret:\n",
    "        break\n",
    "\n",
    "    # Convert to grayscale\n",
    "    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "    # Detect faces\n",
    "    faces = face_cap.detectMultiScale(\n",
    "        gray,\n",
    "        scaleFactor=1.1,\n",
    "        minNeighbors=5,\n",
    "        minSize=(30, 30)\n",
    "    )\n",
    "    # If no face detected\n",
    "    if len(faces) == 0:\n",
    "        cv2.putText(video_data, \"No Person\",\n",
    "                    (50, 50),\n",
    "                    cv2.FONT_HERSHEY_SIMPLEX,a\n",
    "                    1,\n",
    "                    (0, 0, 255),\n",
    "                    2)\n",
    "\n",
    "    # Draw rectangle around faces\n",
    "    for (x, y, w, h) in faces:\n",
    "        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 255, 0), 2)\n",
    "\n",
    "    # Show output\n",
    "    cv2.imshow(\"video_live\", video_data)\n",
    "\n",
    "    # Press 'a' to exit\n",
    "    if cv2.waitKey(10) & 0xFF == ord('a'):\n",
    "        break\n",
    "\n",
    "# Release resources\n",
    "video_cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a2c2e5c9-b6dd-49e6-b344-f3fef418bc9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bebcc03-64bf-4188-9f5c-46965d166d10",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
