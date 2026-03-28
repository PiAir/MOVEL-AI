-- _extensions/private-video/private-video.lua
function Render(args)
  -- If it's a table (from recent pandoc), extracting attributes
  local video_id
  local show_link = true

  if type(args) == "table" then
    video_id = pandoc.utils.stringify(args[1])
    if args["link"] == "false" then
      show_link = false
    end
  else
    video_id = pandoc.utils.stringify(args)
  end

  local thumb_url = "https://img.youtube.com/vi/" .. video_id .. "/hqdefault.jpg"
  local video_url = "https://www.youtube-nocookie.com/embed/" .. video_id .. "?autoplay=1"
  local youtube_watch_url = "https://www.youtube.com/watch?v=" .. video_id

  -- Wrapper div for spacing
  local html = '<div class="private-video-wrapper" style="margin-bottom: 2em;">'

  -- Placeholder div + inline script via DOM
  html = html .. '<div class="video-placeholder" data-embed="' .. video_url .. '" '
  html = html .. 'style="background-image:url(\'' .. thumb_url .. '\');background-size:cover;background-position:center;aspect-ratio:16/9;cursor:pointer;display:flex;align-items:center;justify-content:center;position:relative;">'
  html = html .. '<div style="background:rgba(0,0,0,0.6);color:white;padding:20px;border-radius:10px;text-align:center;pointer-events:none;">'
  html = html .. '<div style="font-size:3em;">&#9654;</div>'
  html = html .. '<p style="margin:0;">Klik om video te starten</p>'
  html = html .. '</div></div>'

  if show_link then
    html = html .. '<div style="margin-top: 0.5em; font-size: 0.9em; text-align: right;">'
    html = html .. '<a href="' .. youtube_watch_url .. '" target="_blank" rel="noopener">Bekijk op YouTube</a>'
    html = html .. '</div>'
  end

  html = html .. '<script>(function(){'
  html = html .. 'var el=document.currentScript.previousElementSibling;'
  -- If link is shown, the script's previous sibling is the link-div, so we need the one before that
  if show_link then
    html = html .. 'el=el.previousElementSibling;'
  end
  html = html .. 'el.addEventListener("click",function(){'
  html = html .. 'var f=document.createElement("iframe");'
  html = html .. 'f.src=el.dataset.embed;'
  html = html .. 'f.style.cssText="position:absolute;top:0;left:0;width:100%;height:100%;border:0";'
  html = html .. 'f.setAttribute("allow","autoplay; encrypted-media");'
  html = html .. 'f.setAttribute("allowfullscreen","");'
  html = html .. 'el.innerHTML="";'
  html = html .. 'el.style.padding="0";'
  html = html .. 'el.appendChild(f);'
  html = html .. '});'
  html = html .. '})();</script>'
  
  html = html .. '</div>' -- close wrapper

  return pandoc.RawBlock('html', html)
end

return {
  ["private-video"] = Render
}
