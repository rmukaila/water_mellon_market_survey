var currentTab = 0; // Current tab is set to be the first tab (0)
showTab(currentTab); // Display the current tab

function showTab(n) {
  // This function will display the specified tab of the form
  var x = document.getElementsByClassName("tab");
  var isDeposit = document.getElementById("id_carddeposit_select").value=="Deposit"
  var email_tab = document.getElementById("id_email_div")
  if (isDeposit && n==6){
    email_tab.style.display = "block";
  }else{
  email_tab.style.display = "none";
  x[n].style.display = "block";}
  // console.log(x)

  //fix the Previous/Next buttons:
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  
  if (n == (x.length - 1) || email_tab.style.display=="block" ) {
    document.getElementById("nextBtn").innerHTML = "Submit";
  } else {
    document.getElementById("nextBtn").innerHTML = "Next";
  }
  //and run a function that displays the correct step indicator:
  fixStepIndicator(n,isDeposit)
}


function nextPrev(n) {
  // This function will figure out which tab to display
  var x = document.getElementsByClassName("tab");  
  var email_tab = document.getElementById("id_email_div");

  // Exit the function if any field in the current tab is invalid:
//   if (n == 1 && !validateForm()) return false; //We pause the validation for now

  // Hide the current tab:
  x[currentTab].style.display = "none";

  // Increase or decrease the current tab by 1:
  currentTab = currentTab + n;

  // if you have reached the end of the form then activate form submission :
  if (currentTab >= x.length) {
    document.getElementById("survForm").submit();
    return false;

   //If you are on email tab and button clicked is "Previous" then activate form submission
   //Note: By default previous, next and submit buttons can submit form if submission is activated.
   //So we needed to use the -/+ increamentation to tell between previous/submit button clicks
   //so as to activate/deactivate form submission correctly

   //check if if prev or next/submit was clicked (+/-) and on email tab
  }else if(n>0 && email_tab.style.display=="block") {
    document.getElementById("survForm").submit();
  return false}

  // Otherwise, display the correct tab:
  showTab(currentTab);
  }


function validateForm() {
  // This function deals with validation of the form fields
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  // A loop that checks every input field in the current tab:
  for (i = 0; i < y.length; i++) {
    // If a field is empty...
    if (y[i].value == "") {
      // add an "invalid" class to the field:
      y[i].className += " invalid";
      // and set the current valid status to false:
      valid = false;
    }
  }
  // If the valid status is true, mark the step as finished and valid:
  // if (valid) {
  //   document.getElementsByClassName("step")[currentTab].className += " finish";
  // }
  return valid; // return the valid status
 }


function fixStepIndicator(n,isDeposit) {
  // This function removes the "active" class of all steps...  
  var i, x = document.getElementsByClassName("step");
  var email_tab = document.getElementById("id_email_div")
  var total_steps = x.length

  //if Deposit is selected instead of Card, hide last two step indicators
  // if (isDeposit ){
    
  //   // console.log(x[total_steps-1])
  //   x[total_steps-1].style.background-color="white" 
  //   x[total_steps-2].style.background-color="white"   
  // }
  // else if (!isDeposit){
  //   x[total_steps-1].style.display="block"
  //   x[total_steps-2].style.display="block"
  // }
  
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }

    //adds the "active" class to the current step:
  //   console.log(x[n])
    x[n].className += " active";
  }
