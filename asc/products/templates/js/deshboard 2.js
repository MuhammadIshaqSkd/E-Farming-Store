  <script type="text/javascript">

//                money received Start
               document.getElementById("amounts").addEventListener("click",function(){

                            document.getElementById('Today').style.display = 'none';
                            document.getElementById('ordercount').style.display = 'flex';
                            document.getElementById('noticfication').style.display = 'none';
                            document.getElementById('allOrders').style.display = 'none';
                            document.getElementById('deilverContainer').style.display = 'none';
                            document.getElementById('threedayscontainer').style.display = 'none';
                            document.getElementById('receivedamount').style.display = 'grid';

                });
//                money received END


//Deilver Profile Open start
     document.getElementById("deilveropen").addEventListener("click",function(){

                            document.getElementById('threedayscontainer').style.display = 'none';

                            document.getElementById('Today').style.display = 'none';
                            document.getElementById('allOrders').style.display = 'none';
                            document.getElementById('receivedamount').style.display = 'none';
                            document.getElementById('ordercount').style.display = 'none';
                             document.getElementById('noticfication').style.display = 'none';

                            document.getElementById('deilverContainer').style.display = 'grid';

                });
//Deilver Profile Open ENDA


    </script>