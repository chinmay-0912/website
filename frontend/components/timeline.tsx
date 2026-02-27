"use client";

import Image from "next/image";
import { motion } from "framer-motion";
import { timelineEvents } from "../data/timelineData";

export default function Timeline() {
  return (
    <section className="relative w-full py-24">

      {/* Vertical Line */}
      <div className="absolute left-1/2 top-0 -translate-x-1/2 w-[4px] bg-gray-700 h-full" />

      <div className="relative max-w-6xl mx-auto space-y-24">

        {timelineEvents.map((event, index) => {
          const isLeft = index % 2 === 0;

          return (
            <motion.div
              key={event.year}
              initial={{ opacity: 0, y: 40 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true, amount: 0.3 }}
              className="group grid grid-cols-[1fr_auto_1fr] items-center"
            >

              {/* LEFT YEAR */}
              <div className={`pr-16 ${isLeft ? "text-right" : "invisible"}`}>
                {isLeft && <Year year={event.year} />}
              </div>

              {/* CENTER DOT */}
              <div className="flex justify-center">
                <div
                  className="
                    w-6 h-6
                    bg-blue-500
                    rounded-full
                    border-4 border-gray-900
                    transition-all duration-300
                    group-hover:scale-110
                    group-hover:shadow-[0_0_20px_6px_rgba(59,130,246,0.6)]
                  "
                />
              </div>

              {/* RIGHT YEAR */}
              <div className={`pl-16 ${!isLeft ? "text-left" : "invisible"}`}>
                {!isLeft && <Year year={event.year} />}
              </div>

              {/* CARD ROW */}
              <div className="col-span-3 grid grid-cols-[1fr_auto_1fr] mt-8">

                {/* LEFT CARD */}
                <div className={`pr-16 ${isLeft ? "" : "invisible"}`}>
                  {isLeft && (
                    <TimelineCard event={event} alignRight />
                  )}
                </div>

                <div />

                {/* RIGHT CARD */}
                <div className={`pl-16 ${!isLeft ? "" : "invisible"}`}>
                  {!isLeft && (
                    <TimelineCard event={event} alignRight={false} />
                  )}
                </div>

              </div>

            </motion.div>
          );
        })}
      </div>
    </section>
  );
}

/* ========================= */
/* YEAR COMPONENT */
/* ========================= */

function Year({ year }: { year: string }) {
  return (
    <h2 className="text-4xl font-light text-gray-500 tracking-widest select-none">
      {year}
    </h2>
  );
}

/* ========================= */
/* CARD COMPONENT */
/* ========================= */

function TimelineCard({
  event,
  alignRight,
}: {
  event: any;
  alignRight: boolean;
}) {
  return (
    <div
      className={`relative group/card w-[340px] h-[220px] ${
        alignRight ? "ml-auto" : ""
      }`}
    >
      {/* IMAGE */}
      <Image
        src={event.imageUrl}
        alt={event.title}
        fill
        className="
          object-cover
          rounded-xl
          transition duration-500
          group-hover/card:scale-105
          group-hover/card:brightness-75
        "
      />

      {/* OVERLAY */}
      <div
        className="
          absolute inset-0
          rounded-xl
          bg-gradient-to-t
          from-black/80
          via-black/50
          to-transparent
          backdrop-blur-[1px]
          opacity-0
          transition-all duration-500
          group-hover/card:opacity-100
          flex flex-col
          justify-end
          px-6 pb-6
        "
      >
        <h3 className="text-lg font-semibold text-white mb-2">
          {event.title}
        </h3>
        <p className="text-sm text-gray-200 leading-relaxed">
          {event.text}
        </p>
      </div>
    </div>
  );
}