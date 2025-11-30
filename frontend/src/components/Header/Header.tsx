import {
  NavigationMenu,
  NavigationMenuContent,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  NavigationMenuTrigger,
} from '@/components/ui/navigation-menu'
import { Link } from '@tanstack/react-router'

export default function Header() {
  return (
    <NavigationMenu viewport={false} className="w-full">
      <NavigationMenuList>
        <NavigationMenuItem>
          <NavigationMenuItem>
            <NavigationMenuTrigger>Texts</NavigationMenuTrigger>
            <NavigationMenuContent>
              <ul className="grid w-[300px] gap-4">
                <li>
                  <NavigationMenuLink asChild>
                    <Link to="/texts">
                      <div className="font-medium">Texts</div>
                      <div className="text-muted-foreground">
                        View your texts
                      </div>
                    </Link>
                  </NavigationMenuLink>
                </li>
              </ul>
            </NavigationMenuContent>
          </NavigationMenuItem>
        </NavigationMenuItem>
      </NavigationMenuList>
    </NavigationMenu>
  )
}
