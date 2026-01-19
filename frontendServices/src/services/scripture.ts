import { apiGet } from "./api";

export interface BibleBook {
  book: number;
  book_name: string;
}

export const getBibleBooks = async (): Promise<BibleBook[]> => {
  return apiGet<BibleBook[]>("/scripture/BibleBooks");
};
