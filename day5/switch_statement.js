let job = "designer";

// if(job==='software developer')
//     {
//         console.log("writes code");
//     }
//     else if(job==='designer')
//         {
//             console.log("makes user interface documents")
//         }
//         else if(job==='cloud engineer')
//             {
//             console.log("manages and deploys cloud resources")
//             }
//             else{
//                 console.log("works directly with customer")
//             }

//writing the same thing in switch statements
switch (job) {
  case "software developer":
    console.log("writes code");
    break;
  case "designer":
    console.log("makes user interface documents");
    break;
  case "cloud engineer":
    console.log("manages and deploys cloud resources");
    break;
  default:
    console.log("works directly with customers");
}
