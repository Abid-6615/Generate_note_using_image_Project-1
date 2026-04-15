import streamlit as st
from PIL import Image
from api_calling import note_genetator, audio_transcription, quiz_generator
st.title("Note Summary and Quiz Generator")
st.markdown("Upload upto 3 images to generate Note summary and Quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload the photos of your note",
                              type=['jpg', 'jpeg', 'png'],
                              accept_multiple_files=True)
    
    pil_images = []
    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

# Image section
    if pil_images:
        if len(images) > 3:
            st.warning("Max image upload limit is 3")
        else:
            col = st.columns(len(images))
            for i, img in enumerate(images):
                with col[i]:
                    st.image(img)
        st.success("Uploded images successfully.")
    
# SelectBox section
    selected = st.selectbox("Enter the difficulty of your quiz",
                          ("Easy", "Medium", "Hard"),
                          placeholder="Choose an option",
                          index=None)
    if selected:
        st.success(f"You select {selected} as defficulty.")
    
# Button section
    pressed = st.button("Click the button to initiate AI",
                        type="primary")


if pressed:
    if not images:
        st.error("You must upload 1 image.")
    if not selected:
        st.error("You must select a defficulty.")

    if images and selected:
        
        # Note container
        with st.container(border=True):
            st.subheader("Your Note")
            with st.spinner("Thinking..."):
                generate_note = note_genetator(pil_images)
                st.markdown(generate_note)

        # Audio container
        with st.container(border=True):
            st.subheader("Audio Transcription")
            with st.spinner("audio generating..."):

                generate_note = generate_note.replace("#", "")
                generate_note = generate_note.replace("*", "")
                generate_note = generate_note.replace("-", "")
                generate_note = generate_note.replace("`", "")

                audio_transcript = audio_transcription(generate_note)
                st.audio(audio_transcript)

        #Quiz container
        with st.container(border=True):
            st.subheader(f"Quiz ({selected}) Difficulty")

            with st.spinner("Making Quiz..."):
                quizzes = quiz_generator(pil_images, selected) 
                st.markdown(quizzes)
            