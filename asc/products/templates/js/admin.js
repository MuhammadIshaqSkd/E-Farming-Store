document.getElementById("orderbtn").addEventListener("click",function(){

                            document.getElementById('orderstatus').style.display = 'flex';
                            document.getElementById('aoumt').style.display = 'none';
                            document.getElementById('riders').style.display = 'none';

});

document.getElementById("cash").addEventListener("click",function(){

                            document.getElementById('orderstatus').style.display = 'none';
                            document.getElementById('riders').style.display = 'none';
                            document.getElementById('aoumt').style.display = 'grid';

});

document.getElementById("riderbtn").addEventListener("click",function(){

                            document.getElementById('orderstatus').style.display = 'none';
                            document.getElementById('aoumt').style.display = 'none';
                            document.getElementById('riders').style.display = 'grid';


});