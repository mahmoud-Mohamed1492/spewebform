import streamlit as st
import webbroswer
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


clisked = st.button('Start')
st.markdown("""
<style>
.st-emotion-cache-1bv3lpx {
    display: inline-flex;
    -webkit-box-align: center;
    align-items: center;
    -webkit-box-pack: center;
    justify-content: center;
    font-weight: 400;
    padding: 0.25rem 0.75rem;
    border-radius: 0.5rem;
    min-height: 38.4px;
    margin: 0px 29%;
    line-height: 1.6;
    color: #ffffff;
    width: 300px;
    user-select: none;
    background-color: #ff0000;
    border: 1px solid #ff0000;
}
</style>
""" , unsafe_allow_html=True)
if clicked :
  webbroswer.open('https://spewebform-u3nsh3aihdfxjdwheyjfq7.streamlit.app/')
  
