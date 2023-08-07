// import Image from "next/legacy/image";

// export default function ProjectItem({data}){

//     const title = data.properties.프로젝트이름.title[0]?.plain_text
    // const github = data.properties.Github.url
//     //const YouTube = data.properties.YouTube.url 유튜브 링크가 있다면 const로 선언
//     const Description = data.properties.Description.rich_text[0]?.plain_text
    // const imgSrc = data.cover.file?.url || data.cover.external.url
    // const 사용언어 = data.properties.사용언어.multi_select



//     return(
//         <div className="flex flex-col m-3 bg-slate-700 rounded-xl w-full">
//             <Image
//                 src={imgSrc}
//                 alt="rounde-t-xl"
//                 width="100%"
//                 height="60%"
//                 layout="responsive"
//                 objectFit="cover"
//                 quality={100}
//             />

//             <div className="p4 flex flex-col">
//             <h1 className="text-2xl font-bold">{title}</h1>
//             <h3 className="mt-4 text-xl">{Description}</h3>
//             <a href={github}>Github 바로가기</a>
//             <div className="flex items-start mt-2">
//                 {사용언어.map((aTag)=>(
//                     <h1 className="px-2 py-1 mr-2 rounded-md bg-sky-200 dark:bg-sky-700 w-30" key={aTag.id}>{aTag.name}</h1>
//                 ))}

//             </div>
//             </div>
            

            
//         </div>
//     );
// }

import Image from "next/legacy/image";

export default function ProjectItem({data}){

    const title=data.properties.프로젝트이름.title[0]?.plain_text
    const github = data.properties.Github.url
//  const YouTube = data.properties.YouTube.url 유튜브 링크가 있다면 const로 선언
    const Description = data.properties.Description.rich_text[0]?.plain_text
    const imgSrc = data.cover.file?.url || data.cover.external.url
    const 사용언어 = data.properties.사용언어.multi_select
    const start = data.properties.WorkPeriod.date.start
    const end = data.properties.WorkPeriod.date.end

    const calculatedPeriod=(start,end) => {
        const startDateStringArray = start.split('-');
        const endDateStringArray = end.split('-');

        var startDate = new Date(startDateStringArray[0], startDateStringArray[1], startDateStringArray[2]);
        var endDate = new Date(endDateStringArray[0], endDateStringArray[1], endDateStringArray[2]);

        console.log(`startDate: ${startDate}`)
        console.log(`endDate: ${endDate}`)

        const diffInMs = Math.abs(endDate - startDate);
        const result = diffInMs / (1000 * 60 * 60 * 24);

        console.log(`기간 : ${result}`)
        return result;
    }


// 밑 클래스 네임에 flex flex-col m-3 bg-slate-700 rounded-xl w-full넣김 안되면
    return (
        <div className="project-card">
            <Image
                className="rounded-t-xl"
                src={imgSrc}
                alt="cover image"
                width="100%"
                height="60%"
                layout="responsive"
                objectFit="cover"
                quality={100}
            />

            <div className="p-4 flex flex-col">
                <h1 className="text-2xl font-bold">{title}</h1>
                <h3 className="mt-4 text-xl">{Description}</h3>
                <a href={github}>Github 바로가기</a>
                <p className="my-1">
                    작업기간 : {start} ~ {end}( {calculatedPeriod(start,end)}일)
                </p>


                <div className="flex items-start mt-2">
                    {사용언어.map((aTag)=>(
                        <h1 className="px-2 py-1 mr-2 rounded-md bg-sky-200 dark:bg-sky-700 w-30" key={aTag.id}>{aTag.name}</h1>
                    ))}
                </div>
            </div>
            

            
        </div>
    );
}