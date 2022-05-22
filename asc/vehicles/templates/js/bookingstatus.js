
<script>
document.getElementById("cancebtn").addEventListener("click",function(){

            document.getElementById('orderdetails').style.display = 'none';

            document.getElementById('confirm').style.display = 'grid';

});
document.getElementById("dismiss").addEventListener("click",function(){

            document.getElementById('orderdetails').style.display = 'grid';

            document.getElementById('confirm').style.display = 'none';

});

</script>
