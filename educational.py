import streamlit as st

st.image('logo.png')
st.markdown("""
<style>
img{
            display: block;
            margin-left: 30px;
            margin-right: 50px;
           width:750px;
            height:200px;
           
}            
</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class = 'container1'>            
<p class = 'title'>SPE SU SC Online Recruitment</p>
</div>
          
           
<style>
.title{
        text-align: center; 
        font-family:Cooper Black;
        color:#ffffff;
        font-size: 35px; 
}
.container1{
        width : 750px;
        border: 3px solid black;
        padding: 0px 1px 0px 1px ;
        margin: 0px 10px 0px 10px;
        border-radius: 15px;
        background : black;  
}                                        
</style>         
""" , unsafe_allow_html=True)

st.markdown("""
<div class = 'container2'>                           
<p class = 'section'>Educational Information</p>
</div> 
            
<style>
.container2{
            width : 750px;
        border: 3px solid blue;
        padding: 0px 1px 0px 1px ;
        margin: 20px 10px 0px 10px;
        border-radius: 15px 15px 0 0;
        background : blue;   
} 
.section{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 40px; 
} 
</style>

""" , unsafe_allow_html=True)

st.markdown("""
<div class = 'container3'>            
<p class = 'note'>Please answer all of the following questions</p>
</div> 
            
<style>
.note{
        text-align: center; 
        font-family:Arial;
        color:#ffffff;
        font-size: 30px;    
}   
.container3{
            width : 750px;
        border: 3px solid lightblue;
        padding: 1px 5px 0px 1px ;
        margin: 0px 10px 30px 10px;
        border-radius: 0 0 15px 15px ;
        background : lightblue;   
} 
</style>

""" , unsafe_allow_html=True)


#--------------------------------------- University ----------------------------------------------------
with st.container():
    university = st.text_input('University : '  , 'Suez University')

st.markdown(
        """
<style>
    div[data-testid="stVerticalBlock"] div[style*="flex-direction: column;"] div[data-testid="stVerticalBlock"] {
    width: 750px;
border: 3px solid black;
padding: 25px 25px ;
margin: 5px 0px 15px 10px;
border-radius: 25px  ;
box-shadow: 5px 5px lightblue;
    }
</style>
""" , unsafe_allow_html=True)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------- Faculty ----------------------------------------------------
with st.container():
    faculty = st.text_input('Faculty : ' )

#--------------------------------------------------------------------------------------------------------

#--------------------------------------- Department ----------------------------------------------------
with st.container():
    department = st.text_input('Department : ' )

#--------------------------------------------------------------------------------------------------------

#--------------------------------------- academic Year ----------------------------------------------------
with st.container():
    level = st.radio(
        "Academic Year : ",
        ["Level 0", "Level 1", "Level 2" , "Level 3" , "Level 4"])
        
#--------------------------------------------------------------------------------------------------------

is_clicked = st.button('Next')

if is_clicked :
    if (university == "") | (faculty == "") | (department == "") | (level == "") :
        st.write('Please , Enter All Educational Information')
    else:
        st.write(f'{university}\n{faculty}\n{department}\n{level}')    