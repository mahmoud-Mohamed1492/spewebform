import streamlit as st
import webbrowser
st.markdown("""
<div class = 'container'>
  <p class = 'title'>Welcome To SPE Family</p>
  <p class = 'form'>SPE SU SC Online Recruitment</p>
  <p class = 'speech'>Please, read the following very carefully.\n\nApplication filling tips:\n\n1- Read the questions very carefully, think about them, then type your answer.\n\n2- Make sure your answer is clear as possible as you can.\n\n3- Take all the time you need to answer the questions, your answers represent you!\n\n\n\nNote that:\n\nIf you are currently an Executive Board or High Board member at another Student Chapter in Suez University, you're not allowed to join SPE Suez.\n\n\n\nFor any inquiries, do not hesitate to contact us on:\n\nspesusc.hrm.2023@gmail.com \n\nThanks in advance!</p>                      
</div> 

<style>
.container{
        width: 900px;
    border: 3px solid black;
    padding: 30px;
    margin: 0px 0px 30px -100px;
    border-radius: 15px;
    background: white;   
}
            
.title{
        text-align: center; 
        font-family:Cooper Black;
        color:#000000;
        font-size: 50px; 
}     

.form{
        text-align: center; 
        font-family:Cooper Black;
        color:#000000;
        font-size: 40px; 
}      

             
</style>            

""" , unsafe_allow_html=True)


is_clicked = st.button('Start')

  
if is_clicked:
    url = 'https://spewebform-u3nsh3aihdfxjdwheyjfq7.streamlit.app/'
    webbrowser.open(url)
    
