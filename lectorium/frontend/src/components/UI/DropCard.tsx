import React from "react";
import styles from "./DropCard.module.scss";
import uploadIcon from "../../assets/icons/upload.svg";

export const DropCard: React.FC = () => {
  return (
    <div>
      <div className={styles.card}>
        <div draggable className={styles.card__drop}>
          <img src={uploadIcon} alt="" />
          <h2 className={styles.drop__title}>Загрузить</h2>
          <span className={styles.drop__desc}>перетащите&nbsp;wav,mp3,ogg</span>
        </div>

        <div className={styles.card__desc}>
          <h2 className={styles.desc__title}>Загрузите&nbsp;аудио</h2>
          <span className={styles.card__span}>Описание</span>
        </div>
      </div>
    </div>
  );
};
