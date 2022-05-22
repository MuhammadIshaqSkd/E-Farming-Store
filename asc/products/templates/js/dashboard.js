
    <script type="text/javascript">

                document.addEventListener("DOMContentLoaded", function(event) {

                        const showNavbar = (toggleId, navId, bodyId, headerId) =>{
                        const toggle = document.getElementById(toggleId),
                        nav = document.getElementById(navId),
                        bodypd = document.getElementById(bodyId),
                        headerpd = document.getElementById(headerId)

                        <!--// Validate that all variables exist-->
                        if(toggle && nav && bodypd && headerpd){
                        toggle.addEventListener('click', ()=>{
                        <!--// show navbar-->
                        nav.classList.toggle('show')
                        <!--// change icon-->
                        toggle.classList.toggle('bx-x')
                        <!--// add padding to body-->
                        bodypd.classList.toggle('body-pd')
                        <!--// add padding to header-->
                        headerpd.classList.toggle('body-pd')
                        })
                        }
                        }

                        showNavbar('header-toggle','nav-bar','body-pd','header')

                        <!--/*===== LINK ACTIVE =====*/-->
                        const linkColor = document.querySelectorAll('.nav_link')

                        function colorLink(){
                        if(linkColor){
                        linkColor.forEach(l=> l.classList.remove('active'))
                        this.classList.add('active')
                        }
                        }
                        linkColor.forEach(l=> l.addEventListener('click', colorLink))

                    <!--// Your code to run since DOM is loaded and ready-->


                });

                //Order today Start visible  {{Okay}}
                document.getElementById("todayopen").addEventListener("click",function(){

                            document.getElementById('Today').style.display = 'grid';
                            document.getElementById('ordercount').style.display = 'flex';
                            document.getElementById('noticfication').style.display = 'none';
                            document.getElementById('allOrders').style.display = 'none';
                            document.getElementById('deilverContainer').style.display = 'none';
                            document.getElementById('threedayscontainer').style.display = 'none';
                            document.getElementById('receivedamount').style.display = 'none';

                });
                //Order today END visible



                //All Order  Start visible {{Okay}}
                document.getElementById("allorderss").addEventListener("click",function(){

                            document.getElementById('Today').style.display = 'none';
                            document.getElementById('threedayscontainer').style.display = 'none';
                            document.getElementById('receivedamount').style.display = 'none';
                            document.getElementById('deilverContainer').style.display = 'none';
                            document.getElementById('noticfication').style.display = 'none';
                            document.getElementById('allOrders').style.display = 'grid';
                            document.getElementById('ordercount').style.display = 'flex';

                });
                //All Order END visible

                //Threedays Order  Start visible
                document.getElementById("missed").addEventListener("click",function(){

                            document.getElementById('threedayscontainer').style.display = 'grid';
                            document.getElementById('receivedamount').style.display = 'none';
                            document.getElementById('Today').style.display = 'none';
                            document.getElementById('noticfication').style.display = 'none';
                            document.getElementById('ordercount').style.display = 'flex';
                            document.getElementById('deilverContainer').style.display = 'none';
                            document.getElementById('allOrders').style.display = 'none';

                });
                //Threedays Order END visible








//Notification start
     document.getElementById("notific").addEventListener("click",function(){

                            document.getElementById('threedayscontainer').style.display = 'none';

                            document.getElementById('Today').style.display = 'none';
                            document.getElementById('allOrders').style.display = 'none';
                            document.getElementById('receivedamount').style.display = 'none';
                            document.getElementById('ordercount').style.display = 'none';

                            document.getElementById('deilverContainer').style.display = 'none';
                            document.getElementById('deilverContainer').style.display = 'none';
                            document.getElementById('noticfication').style.display = 'grid';

                });
//Notification   ENDA


    </script>