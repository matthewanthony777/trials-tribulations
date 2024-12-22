import Image from 'next/image'
import authorImage from '@/public/images/authors/matthew.jpg'

export default function Intro() {
  return (
    <section className='flex flex-col-reverse items-start gap-x-10 gap-y-4 pb-24 md:flex-row md:items-center'>
      <div className='mt-2 flex-1 md:mt-0'>
        <h1 className='title no-underline'>Matthew Anthony Barr.</h1>
        <p className='mt-3 font-light text-muted-foreground'>
          As a Technology professional, Advocate, and  Writer, I explore all things Media, Law and Technology. Through my projects and commentary, i illuminate complex stories and examine the dynamic impacts of these fields, weaving together insights and projects that inspire, inform and drive meaningful change.
          
        </p>
      </div>
      <div className='relative'>
        <Image
          className='flex-1 rounded-lg grayscale'
          src={authorImage}
          alt='Matthew Anthony Barr'
          width={175}
          height={175}
          priority
        />
      </div>
    </section>
  )
}
