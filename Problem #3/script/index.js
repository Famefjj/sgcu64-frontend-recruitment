const form = document.getElementById("register-form")
form.addEventListener("submit", event => {
  event.preventDefault()
  const formData = new FormData(form)
  const data = {}
  for (const [key, value] of formData.entries()) {
    /* USER CODE Begin: Validate data */
    const re = /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i;
    if ((value === "") || (value == null)){
      alert('Please provide your '+ key +" !")
      return false
    }
    else if ((key === "email") && !re.test(String(value).toLowerCase())){
      alert("Your email is incorrect !")
      return false
    }
    else if ((key === "confirmpassword") && (value !== data["password"])){
      alert("Your confirm password not equal to password !")
      return false
    }
    else if ((key === "password") && (value.length < 6)){
      alert('Your password must contain at least 5 characters')
      return false
    }
    else {
      data[key] = value
    }
    /* USER CODE Begin: Validate data */
  }
  console.log(data)
  /* USER CODE Begin: What happened next after recieve form data (Optional) */
  form.submit()
  /* USER CODE END: What happened next after recieve form data (Optional) */
})
