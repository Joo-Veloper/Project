//원본
// import Layout from "../components/layout";
// import Head from "next/head";
// import { TOKEN, DATABASE_ID } from "@/config";

// export default function Projects({projectNames}){
//     console.log(projectNames);  

//     return(
//         <Layout>
//             <Head>
//                 <title>박승주의 포트폴리오</title>
//                 <meta name="description" content="오늘도 빡코딩" />
//                 <meta name="viewport" content="width=device-width, initial-scale=1" />
//                 <link rel="icon" href="/favicon.ico" />
//             </Head>
//             <h1>프로젝트</h1>
//         </Layout>
//     );
// }

// //빌드타임에 호출
// export async function getStaticProps() {    
//     const options = {
//         method: 'POST',
//         headers: {
//             'Accept': 'application/json',
//             'Notion-Version': '2022-06-28',
//             'content-type': 'application/json',
//             'Authorization': `Bearer ${TOKEN}`
//         },
//         body: JSON.stringify({page_size: 100})
//       };
      
//     const res = await fetch(`https://api.notion.com/v1/databases/${DATABASE_ID}/query`, options)
    
//     const projects = await res.json()
    
    

//     const projectNames = projects.results.map((aProject) =>(
//         aProject.properties.프로젝트이름.title[0]?.plain_text
        
//     ))

//     console.log(`projectNames : ${projectNames}`);

    
//     return {
//       props: {projectNames},
//     }
//   }

//Test2(2번째원본)

// import Layout from "../components/layout";
// import Head from "next/head";
// import { TOKEN, DATABASE_ID } from "@/config";
// import ProjectItem from "@/components/projects/project-item";


// export default function Projects({projects}){
//     console.log(projects);  

//     return(
//         <Layout>
//             <div className="flex flex-col items-center justify-center min-h-screen mb-10 px-6">
//                 <Head>
//                     <title>박승주의 포트폴리오</title>
//                     <meta name="description" content="오늘도 빡코딩" />
//                     <meta name="viewport" content="width=device-width, initial-scale=1" />
//                     <link rel="icon" href="/favicon.ico" />
//                 </Head>
//                 <h1 className="text-4xl font-bold sm:text-6xl">
//                     총 프로젝트:
//                     <span className="pl-4 text-blue-500">{projects.results.length}</span>
//                 </h1>

//                 <div className="grid grid-cols-1 md:grid-cols-2 py-10 m-6 gap-8 w-full">
//                     {projects.results.map((aProject) => 
//                             <ProjectItem key={aProject.id} data={aProject}/>
//                     )}
//                 </div>
//             </div>
            

            
//         </Layout>
//     );
// }

// //빌드타임에 호출
// export async function getStaticProps() {    
//     const options = {
//         method: 'POST',
//         headers: {
//             'Accept': 'application/json',
//             'Notion-Version': '2022-06-28',
//             'content-type': 'application/json',
//             'Authorization': `Bearer ${TOKEN}`
//         },
//         body: JSON.stringify({
//             sorts: [
//                 {
//                     "property": "프로젝트이름",
//                     "direction": "ascending"

//                 }
//             ],
//             page_size: 100
//         })
//       };
      
//     const res = await fetch(`https://api.notion.com/v1/databases/${DATABASE_ID}/query`, options)
    
//     const projects = await res.json()
    
    

//     const projectNames = projects.results.map((aProject) =>(
//         aProject.properties.프로젝트이름.title[0]?.plain_text        
//     ))

//     console.log(`projectNames : ${projectNames}`);

    
//     return {
//       props: {projects},
//     }
//   }


//test3

// import Layout from "../components/layout";
// import Head from "next/head";
// import { TOKEN, DATABASE_ID } from "@/config";

// export default function Projects({projects}){
//     console.log(projects);  

//     return(
//         <Layout>
//             <Head>
//                 <title>박승주의 포트폴리오</title>
//                 <meta name="description" content="오늘도 빡코딩" />
//                 <link rel="icon" href="/favicon.ico" />
//             </Head>
//             <h1>총 프로젝트 : {projects.results.length}</h1>

//             {projects.results.map((aProject)=>(
//                 <h1>{aProject.properties.프로젝트이름.title[0]?.plain_text}</h1>
//             ))}
//         </Layout>
//     );
// }

// //빌드타임에 호출
// export async function getStaticProps() {    
//     const options = {
//         method: 'POST',
//         headers: {
//             'Accept': 'application/json',
//             'Notion-Version': '2022-06-28',
//             'content-type': 'application/json',
//             'Authorization': `Bearer ${TOKEN}`
//         },
//         body: JSON.stringify({
//             sorts: [
//                 {
//                     "property": "프로젝트이름",
//                     "direction": "descending"

//                 }
//             ],
//             page_size: 100
//         })
//       };
      
//     const res = await fetch(`https://api.notion.com/v1/databases/${DATABASE_ID}/query`, options)
    
//     const projects = await res.json()
    
    

//     const projectNames = projects.results.map((aProject) =>(
//         aProject.properties.프로젝트이름.title[0]?.plain_text
        
//     ))

//     console.log(`projectNames : ${projectNames}`);

    
//     return {
//       props: {projects},
//     }
//   }

//화면만들기 test4

import Layout from "../components/layout";
import Head from "next/head";
import { TOKEN, DATABASE_ID } from "@/config";
import ProjectItem from "@/components/projects/project-item";

export default function Projects({projects}){
    console.log(projects);  

    return(
        <Layout >
            <div className="flex flex-col items-center jsutify-center min-h-screen mb-10 px-6">
                <Head>
                    <title>박승주의 포트폴리오</title>
                    <meta name="description" content="오늘도 빡코딩" />
                    <link rel="icon" href="/favicon.ico" />
                </Head>
                <h1 className="text-4xl font-bold sm:text-6xl">
                    총 프로젝트 : 
                    <span className="pl-4 text-blue-500">{projects.results.length}</span>
                </h1>

                {/* md:grid= gird숫자늘리수 있음 */}
                <div className="grid grid-cols-1 md:grid-cols-3 py-10 m-6 gap-8">  
                    {projects.results.map((aProject)=>(
                        <ProjectItem key={aProject.id} data={aProject}/>
                    ))}
                </div>

            </div>
            
            
        </Layout>
    );
}

//빌드타임에 호출
export async function getStaticProps() {    
    const options = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Notion-Version': '2022-06-28',
            'content-type': 'application/json',
            'Authorization': `Bearer ${TOKEN}`
        },
        body: JSON.stringify({
            sorts: [
                {
                    "property": "프로젝트이름",
                    "direction": "descending"

                }
            ],
            page_size: 100
        })
      };
      
    const res = await fetch(`https://api.notion.com/v1/databases/${DATABASE_ID}/query`, options)
    
    const projects = await res.json()
    
    

    const projectNames = projects.results.map((aProject) =>(
        aProject.properties.프로젝트이름.title[0]?.plain_text
        
    ))

    console.log(`projectNames : ${projectNames}`);

    
    return {
      props: {projects},
    }
  }