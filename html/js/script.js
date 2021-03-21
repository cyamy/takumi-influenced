$(function () {
  $(window).on("load resize", function () {
    let i = 1;
    while ($(".artist-title-mod" + i).length){
      const current_class = $(".artist-title-mod" + i);
      const inner_width = parseInt(current_class.innerWidth());
      const char_size = parseInt(current_class.find("h2").css("font-size"));
      const char_count = current_class.find("h2").text().length;

      const char_width = char_size * char_count;

      if(inner_width < char_width){

        let mod_char_width = char_width;
        while (inner_width <= mod_char_width) {
          mod_char_width--;
        }
        $(".artist-title-mod" + i).find("h2").css("font-size", (mod_char_width / char_count) * 1.5 + "px");
        // source code proのアスペクト比が大体0.6:1なので1.5倍に
      }
      i++;
    }
  });
});
