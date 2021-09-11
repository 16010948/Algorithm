class Solution {
    static final int SIZE = 5;
    static final int OK = 1;
    static final int NO = 0;
    static final int[][] DELTA = {{-1, 0}, {0, -1}, {1, 0}, {1, 0}};

    static int getDistance(int[] position1, int[] position2) {
        return Math.abs(position1[0] - position2[0]) + Math.abs(position1[1] - position2[1]);
    }

    static int isPossible(String[] place) {
        int [][] position = new int[SIZE * SIZE][2];
        int index = 0;
        for(int y = 0; y < SIZE; y++) {
            for(int x = 0; x < SIZE; x++) {
                if(place[y].charAt(x) == 'P'){
                    position[index++] = new int[]{y, x};
                }
            }
        }

        for(int i = 0; i < index; i++) {
            for(int j = i + 1; j < index; j++) {
                int distance = getDistance(position[i], position[j]);
                if(distance == 1) {
                   return NO;
                } else if(distance == 2){
                    if(position[i][0] == position[j][0] || position[i][1] == position[j][1]) {
                        int ny = (int)((position[j][0] + position[i][0]) / 2.0);
                        int nx = (int)((position[j][1] + position[i][1]) / 2.0);
                        if(place[ny].charAt(nx) != 'X') return NO;
                    } else {
                        if(place[position[i][0]].charAt(position[j][1]) != 'X') return NO;
                        if(place[position[j][0]].charAt(position[i][1]) != 'X') return NO;
                    }
                }
            }
        }

        return OK;
    }

    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        for(int i = 0; i < places.length; i++) {
            answer[i] = isPossible(places[i]);
        }
        return answer;
    }
}