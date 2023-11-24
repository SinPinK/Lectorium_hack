import React from "react";
import styles from "./DropCard.module.scss";
import uploadIcon from "../../assets/icons/upload.svg";
import { useState } from "react";

export const DropCard: React.FC = () => {
  const [drag, setDrag] = useState(false);

  const dragStartHandler = (e:React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setDrag(true);
  };

  const dragLeaveHandler = (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setDrag(false);
  };

  const onDropHandler = (e: any) => {
    e.preventDefault();
    let files = [...e.dataTransfer.files]
    console.log(files);
    setDrag(false)
  }

  return (
    <div>
      <div className={styles.card}>
        {drag ? (
          <div
            onDragStart={(e) => dragStartHandler(e)}
            onDragLeave={(e) => dragLeaveHandler(e)}
            onDragOver={(e) => dragStartHandler(e)}
            onDrop={(e) => onDropHandler(e)}
            className={styles.drop__active}
          >
            <img src={uploadIcon} alt="" />
            <h2 className={styles.drop__title}>
              Отпустите&nbsp;для&nbsp;загрузки
            </h2>
            <span className={styles.drop__desc}>
              перетащите&nbsp;wav,mp3,ogg
            </span>
          </div>
        ) : (
          <div
            onDragStart={(e) => dragStartHandler(e)}
            onDragLeave={(e) => dragLeaveHandler(e)}
            onDragOver={(e) => dragStartHandler(e)}
            className={styles.card__drop}
          >
            <img src={uploadIcon} alt="" />
            <h2 className={styles.drop__title}>Загрузить</h2>
            <span className={styles.drop__desc}>
              перетащите&nbsp;wav,mp3,ogg
            </span>
          </div>
        )}

        <div className={styles.card__desc}>
          <h2 className={styles.desc__title}>Загрузите&nbsp;аудио</h2>
          <span className={styles.card__span}>Описание</span>
        </div>
      </div>
    </div>
  );
};
