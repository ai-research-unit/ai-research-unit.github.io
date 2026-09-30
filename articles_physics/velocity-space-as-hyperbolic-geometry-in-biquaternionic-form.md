# __Velocity Space as Hyperbolic Geometry in Biquaternionic Form__

## Introduction

A Lorentz boost is fixed by a velocity, so the set of boosts is the set of velocities; and that set is not a vector space. It has a boundary, the light cone, which no boost reaches; the composition of two boosts is not the parallelogram rule; and a closed path of boosts need not return the spin, the residue being the Wigner rotation. These three facts are one fact, and the fact is geometric: the velocity space of a massive particle is a **hyperbolic three-space of curvature $-1/c^2$**. In it the rapidity is the geodesic distance from rest, the light cone is the boundary at infinity, the velocity-addition law is the trigonometry of geodesic triangles, and the Wigner rotation is the curvature of the boost connection, with an angle equal to the hyperbolic area the loop encloses.

The framework already carries the manifold. The four-velocity is a unit timelike element of the material sector, so its tip runs over the future sheet of the quadric $N(\tilde{U}) = -c^2$ in $\mathbb{M}_-$; the boost manifold is the symmetric space $\mathcal{B}\cong SL(2,\mathbb{C})/SU(2)\cong\mathbb{H}^3$; and the rapidity is the additive coordinate on each line through the rest point. What the framework does not carry is the **metric** of that manifold, its distance function, its trigonometry, and the identification of the velocity-addition law with its geometry. Those are the subject of this article, and they are supplied in the algebra's own coordinates.

The construction is the hyperbolic geometry of the velocity hyperboloid, in the form given by Varićak and Sommerfeld and developed in the modern literature by Ungar and by Rhodes and Semon; the immediate source for the account followed here is Barrett's conference paper on Minkowski space-time and hyperbolic geometry, and the monograph that develops the same material at length, whose statements have been re-derived in the framework's conventions and checked numerically. The claim it rests on is old and is Borel's, quoted as the epigraph of the monograph: *the principle of relativity corresponds to the hypothesis that the kinematic space is a space of constant negative curvature, and the value of the radius of curvature is the speed of light*. Two things beyond the classical account are the framework's own. First, the **boundary at infinity is the zero-divisor cone**, so the ideal points of the geometry are exactly the lightlike elements, the ones the algebra cannot invert; the cross-ratio that defines the metric is built from them. Second, the **holonomy of a closed boost path is the hyperbolic area of the loop's rapidity triangle**, which turns the numerical drift recorded in the companion article on the Wigner rotation into an exact identity with a computable correction.

The findings are stated in advance.

1. **Velocity space is a hyperboloid of curvature $-1/c^2$.** The four-velocity runs over the quadric $N(\tilde{U}) = -c^2$ in $\mathbb{M}_-$ with the $ict$ metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$; in Weierstrass coordinates $\tilde{U} = c(\sinh(\rho/c)\,\hat{\mathbf{u}}+i\cosh(\rho/c)\,e_0)$ the radial coordinate $\rho$ is the geodesic distance from rest and the rapidity is $\psi = \rho/c$.
2. **The metric is the Beltrami–Klein metric** in the velocity coordinates, $ds^2 = c^2[(c^2-\mathbf{v}^2)|d\mathbf{v}|^2+(\mathbf{v}\cdot d\mathbf{v})^2]/(c^2-\mathbf{v}^2)^2$, and the distance between two velocities is the relative rapidity: $\cosh(d/c) = \gamma_1\gamma_2(1-\mathbf{v}_1\cdot\mathbf{v}_2/c^2)$.
3. **The addition of velocities is hyperbolic trigonometry.** The relative-velocity formula is the hyperbolic law of cosines in velocity space, and the composition law of two boosts is its spherical counterpart, the two being exchanged by $c\mapsto ic$ — the Sommerfeld spherical representation.
4. **The Wigner rotation is the curvature of the boost connection.** Its angle is the hyperbolic area of the geodesic triangle whose sides are the three rapidities of the loop; the Euclidean area $\tfrac12 ab$ is the leading term, and the correction is $-\tfrac{1}{24}ab(a^2+b^2)$.
5. **The light cone is the boundary at infinity.** It is at infinite geodesic distance from every velocity while the velocity itself is bounded by $c$: the rapidity is unbounded where the velocity is bounded, and that is the geometric statement that no finite number of boosts reaches $c$.

The notation is that of the foundational articles: $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, quaternion units $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_1e_2 = e_3$, central scalar $i$, biquaternion norm $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$, Hermitian sector $\mathbb{M}_+$, anti-Hermitian sector $\mathbb{M}_-$. The material coordinate is $\tilde{Q} = ict\,e_0+\mathbf{x}$ with the $ict$ metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$, so that $N(d\tilde{Q}) = -c^2dt^2+d\mathbf{x}^2$. The four-velocity is
$$
\tilde{U} = \gamma(ic\,e_0+\mathbf{v}),\qquad N(\tilde{U}) = -c^2,\qquad \gamma = \Bigl(1-\frac{\mathbf{v}^2}{c^2}\Bigr)^{-1/2},
$$
and the boost rotor is
$$
\tilde{\Lambda} = \cosh\frac{\psi}{2}\,e_0+i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}} = e^{(\psi/2)\,i\hat{\mathbf{u}}},
\qquad N(\tilde{\Lambda}) = 1,\qquad \tanh\psi = \frac{u}{c},
$$
Hermitian and of unit norm. Throughout, $c$ is the speed of light in the medium, $\mathbf{v}$ a particle velocity, $\rho$ the geodesic distance in velocity space and $\psi = \rho/c$ the rapidity.

The companion articles supply the pieces:

- *The Relativistic Particle in Biquaternionic Form*, for the four-velocity, the rapidity and the statement that the four-velocity tip is the hyperboloid $N(\tilde{U}) = -c^2$.
- *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*, for the boost manifold $\mathcal{B}\cong\mathbb{H}^3$, its contractibility and the non-closure of the boosts.
- *The Wigner Rotation and the Information Content of a Boost in Biquaternionic Form*, for the Wigner rotation, the closed-loop holonomy and the numerical angles reproduced below.
- *The Light Cone as the Biquaternion Zero-Divisor Cone*, for the cone $N(\tilde{Q}) = 0$ and its two families.
- *The Lorentz Transformation as a Biquaternionic Rotation*, for the rotor conjugation and the square-root relation between the rotor and the four-velocity.
- Maths article *Hyperbolic Geometry*, for the hyperboloid model, the Weierstrass coordinates and the Cayley–Klein metric, whose pure-geometry statements are used here without re-derivation.

## The Velocity Manifold

### The four-velocity hyperboloid

The four-velocity is a unit timelike element: $N(\tilde{U}) = -c^2$, identically in $\mathbf{v}$, so as the three components of $\mathbf{v}$ range over the open ball $|\mathbf{v}|<c$ the tip of $\tilde{U}$ runs over a three-dimensional quadric in the real four-space $\mathbb{M}_-$. Written in the real coordinates $(\gamma c, \gamma\mathbf{v})$ the quadric is
$$
(\gamma c)^2-\gamma^2\mathbf{v}^2 = c^2\gamma^2\Bigl(1-\frac{\mathbf{v}^2}{c^2}\Bigr) = c^2 ,
$$
that is
$$
c^2t^2-\mathbf{x}^2 = c^2 ,
$$
the **future sheet** of the hyperboloid of unit timelike vectors. Its vertex is the rest point $\tilde{U}_0 = ic\,e_0$.

The restriction of the ambient form to this quadric is Riemannian, and this is worth one line because the sign depends on the convention. In the $ict$ metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ the one negative direction is the time axis, and at a point $X$ of the sheet that direction is represented by the position vector $X$ itself — which is normal to the quadric and not tangent to it. The restriction of $\eta$ to $X^\perp$ is therefore positive definite, with no sign to repair. This is the mirror of the convention of the maths article *Hyperbolic Geometry*, where the form carries the opposite overall sign and the metric on the hyperboloid is the negative of the restricted form; the two descriptions are the two signs of the same metric, and no physical statement depends on the choice.

### Weierstrass coordinates and the rapidity as distance

The quadric may be parametrised by the polar coordinates of the geometry itself. Let $\rho\ge0$ be the distance from the vertex along the sheet and let $\hat{\mathbf{u}}$ be the direction; the **Weierstrass coordinates** of the point are
$$
\tilde{U} = c\Bigl(\sinh\frac{\rho}{c}\,\hat{\mathbf{u}}+i\cosh\frac{\rho}{c}\,e_0\Bigr),
$$
and the normalisation is an identity,
$$
c^2\Bigl(-\cosh^2\frac{\rho}{c}+\sinh^2\frac{\rho}{c}\Bigr) = -c^2 ,
$$
so the pair $(\rho,\hat{\mathbf{u}})$ does parametrise the sheet. Comparing with $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$ gives the dictionary
$$
\gamma = \cosh\frac{\rho}{c},\qquad \mathbf{v} = c\tanh\frac{\rho}{c}\,\hat{\mathbf{u}},\qquad \rho = c\,\mathrm{artanh}\frac{v}{c} = c\psi ,
$$
which is the *hyperbolic velocity* of the classical account: it is what the ordinary velocity becomes when the additive variable is used, and it reduces to $v$ for $v\ll c$.

**Proposition.** In Weierstrass coordinates the induced metric of the velocity hyperboloid is
$$
ds^2 = d\rho^2+c^2\sinh^2\frac{\rho}{c}\;d\Omega^2 ,
$$
where $d\Omega^2$ is the round metric of the unit sphere on the direction.

**Proof.** With $\hat{\mathbf{u}}$ a unit vector, $\hat{\mathbf{u}}\cdot d\hat{\mathbf{u}} = 0$ and $|d\hat{\mathbf{u}}|^2 = d\Omega^2$. Differentiating, $d(c\sinh(\rho/c)\,\hat{\mathbf{u}}) = \cosh(\rho/c)\,\hat{\mathbf{u}}\,d\rho+c\sinh(\rho/c)\,d\hat{\mathbf{u}}$ and $d(c\cosh(\rho/c)) = \sinh(\rho/c)\,d\rho$, whence
$$
-ds^2 = N(d\tilde{U}) = -\sinh^2\frac{\rho}{c}\,d\rho^2+\cosh^2\frac{\rho}{c}\,d\rho^2+c^2\sinh^2\frac{\rho}{c}\,|d\hat{\mathbf{u}}|^2 ,
$$
which is the stated metric.

The metric is the Lobachevsky metric of curvature $-1/c^2$, and $\rho$ is the geodesic distance. Two features of it are the whole of the geometry. The angular coefficient $\sinh^2(\rho/c)$ grows exponentially, so circles of radius $\rho$ have circumference $2\pi c\sinh(\rho/c)$ and the space opens faster than any Euclidean space of the same radius. And the coefficient has the series
$$
c^2\sinh^2\frac{\rho}{c} = \rho^2+\frac{\rho^4}{3c^2}+\cdots ,
$$
so a small ball is Euclidean with a positive fourth-order correction; for the sphere of the same radius the correction is $-\rho^4/3c^2$. The two families are exchanged by $c\mapsto ic$ at fixed $\rho$, which is the interchange of the hyperbolic and the circular functions and the algebraic form of the sign of the ambient form.

### The metric in the velocity coordinates

The sheet is usually described not by $(\rho,\hat{\mathbf{u}})$ but by the velocity $\mathbf{v}$ itself, which is the Beltrami–Klein coordinate of the model — the central projection of the sheet onto the plane $t = \mathrm{const}$, in which the geodesics are straight chords and the ball $|\mathbf{v}|<c$ is the whole of velocity space. Substituting $\mathbf{v} = c\tanh(\rho/c)\hat{\mathbf{u}}$ into the metric gives
$$
ds^2 = c^2\;\frac{(c^2-\mathbf{v}^2)\,|d\mathbf{v}|^2+(\mathbf{v}\cdot d\mathbf{v})^2}{(c^2-\mathbf{v}^2)^2} .
$$

The metric is not the Euclidean metric of the ball and not the Minkowski metric of any spacetime; it is a Riemannian metric on the abstract space of velocities, with the units of a velocity squared. Its distance is a velocity, and its curvature is $-1/c^2$. This is the precise sense in which the set of velocities is not a vector space: a vector space has a flat metric in its linear coordinates, and the metric above is not flat.

## The Distance Between Two Velocities

### The Cayley–Klein distance

The distance in this metric is the **relative rapidity**, and it has three equivalent forms.

**Proposition.** For two velocities $\mathbf{v}_1,\mathbf{v}_2$ of the ball, the geodesic distance between them is given by
$$
\cosh\frac{d}{c} = \frac{c^2-\mathbf{v}_1\cdot\mathbf{v}_2}{\sqrt{(c^2-\mathbf{v}_1^2)(c^2-\mathbf{v}_2^2)}} = \gamma_1\gamma_2\Bigl(1-\frac{\mathbf{v}_1\cdot\mathbf{v}_2}{c^2}\Bigr) ,
$$
and $d = c\,\mathrm{artanh}(v_{\mathrm{rel}}/c)$, where $v_{\mathrm{rel}}$ is the speed of $\mathbf{v}_2$ in the rest frame of $\mathbf{v}_1$.

**Proof.** The first equality is the Beltrami–Klein disc formula of the maths article *Hyperbolic Geometry*; the second is the identity $\gamma = \cosh(\rho/c)$ and $\mathbf{v} = c\tanh(\rho/c)\hat{\mathbf{u}}$, which turns the numerator into the hyperbolic cosine rule and the two roots into $\cosh$'s. For the third, the four-velocity of $\mathbf{v}_1$ is $\tilde{U}_1 = \gamma_1(ic\,e_0+\mathbf{v}_1)$; the speed of $\mathbf{v}_2$ in the frame of $\mathbf{v}_1$ is $\mathbf{v}_{\mathrm{rel}}$, with $\gamma_{\mathrm{rel}} = \gamma_2\gamma_1(1-\mathbf{v}_1\cdot\mathbf{v}_2/c^2)$, which is the second expression again.

The right-hand side is $\ge1$ by the reversed Cauchy inequality, with equality exactly when the two velocities coincide, so the expression is a distance. The cross-ratio form is the same quantity: for the two points of the ball and the two points $a,b$ in which the chord through them meets the boundary $|\mathbf{v}| = c$, ordered $a,\mathbf{v}_1,\mathbf{v}_2,b$,
$$
d(\mathbf{v}_1,\mathbf{v}_2) = \frac{c}{2}\Bigl|\log\frac{|\mathbf{v}_1a|\,|\mathbf{v}_2b|}{|\mathbf{v}_1b|\,|\mathbf{v}_2a|}\Bigr| .
$$
The boundary points are the lightlike ends of the chord, and this is why the metric of velocity space is the **Cayley–Klein metric**: a metric is obtained from the cross-ratio of the points with the *absolute*, and the absolute of velocity space is the light cone.

### The relative-velocity formula as a distance

The classical formula that this packages is the relative velocity of two particles. Writing $\theta$ for the angle between the two velocities, the definition $v_{\mathrm{rel}} = c\tanh(d/c)$ inverts the proposition into
$$
\cosh\frac{d}{c} = \cosh\psi_1\cosh\psi_2-\cos\theta\,\sinh\psi_1\sinh\psi_2 ,
$$
and the relative speed is the fourth side of the relation, $v_{\mathrm{rel}} = c\tanh(d/c)$ with
$$
v_{\mathrm{rel}} = \frac{\sqrt{(\mathbf{v}_1-\mathbf{v}_2)^2-\tfrac{1}{c^2}(\mathbf{v}_1\times\mathbf{v}_2)^2}}{1-\mathbf{v}_1\cdot\mathbf{v}_2/c^2} .
$$
Read as a statement of geometry rather than of kinematics, this is the **hyperbolic law of cosines** of the geodesic triangle whose vertices are the rest point and the two velocity points, with the angle $\theta$ at the rest point. The third side of that triangle is the distance between the two velocities; the formula is the law of cosines written for it; and the law holds because the space in which the triangle is drawn has constant curvature $-1/c^2$. The three vertices are the rest frame and the two particles' frames, and the side lengths are the three rapidities — a triangle in velocity space is the picture of the relative motion of three frames.

**Numerical check.** For $\mathbf{v}_1 = 0.6c\,\hat{\mathbf{x}}$ and $\mathbf{v}_2 = 0.8c\,\hat{\mathbf{y}}$, the proposition gives $\cosh(d/c) = 1.25\times1.6667 = 2.08333$ and $d = 1.36379c$, whence $v_{\mathrm{rel}} = c\tanh 1.36379 = 0.87727c$; the direct velocity-subtraction formula gives the same to machine precision.

## The Addition of Velocities Is Hyperbolic Trigonometry

### Collinear composition

For two boosts along the same line the composition is the degenerate triangle in which the three vertices are collinear in the geometry and the sides add. The rapidity is additive,
$$
\psi_{\mathrm{tot}} = \psi_1+\psi_2,\qquad v_{\mathrm{tot}} = c\tanh(\psi_1+\psi_2) = \frac{v_1+v_2}{1+v_1v_2/c^2},
$$
which is Einstein's addition law, and the statement that the additive variable is the *arc length* in velocity space and not the velocity is the statement that the composition is not vector addition: a vector space would give $\mathbf{v}_{\mathrm{tot}} = \mathbf{v}_1+\mathbf{v}_2$, and the geodesic parametrised by arc length gives the formula above instead. The bound $v<c$ is the statement that the geodesic does not reach the boundary in finite arc length.

**The algebraic form of the collinear law.** In the algebra the same law is a single product. The proper velocity $u=\gamma(e_0+\beta\hat{\mathbf{v}})$ is a unimodular paravector, and the composition is $u_{\mathrm{tot}}=u_2u_1$, whose scalar part is the product of the two Lorentz factors and whose vector part is the composed velocity; the two displayed formulas are the two parts of that product. The product form, with the paravector reading, the four-velocity relation and the boost rule, is *Paravectors and the Geometry of Spacetime*; it is what makes the collinear composition a multiplication rather than a trigonometric computation.

### The composition law and the spherical representation

For two boosts along different directions the composition is not a single boost, and the composed *frame* has a rapidity fixed by the same trigonometry. Let the first boost have rapidity $a$ along $\hat{\mathbf{n}}_1$ and the second rapidity $b$ along $\hat{\mathbf{n}}_2$, with $\theta$ the angle between the two directions. Then the rapidity $\rho$ of the frame reached satisfies
$$
\cosh\rho = \cosh a\cosh b+\cos\theta\,\sinh a\,\sinh b ,
$$
the **spherical** law of cosines-type relation — the plus sign — while the *distance* between the two frames' velocities has the minus sign above. The two laws are the two faces of one identity: they are exchanged by $\cos\theta\mapsto-\cos\theta$, and equivalently by $c\mapsto ic$ at fixed rapidities, which is exactly the Sommerfeld interchange between the Lobachevsky and the spherical representation of the velocity composition — the velocities are added on the surface of a sphere of imaginary radius, and the imaginary radius is the $R\mapsto iR$ of Taurinus (1826). The framework's own form of the interchange is the Weierstrass one recorded above: the hyperbolic and the circular functions are the same functions at $c$ and at $ic$.

Two limits fix the rule. For $\theta = 0$ the composition law reduces to $\cosh(a+b)$, the collinear case. For $\theta = \pi/2$ it reduces to $\cosh\rho = \cosh a\cosh b$, so two perpendicular boosts of rapidities $a$ and $b$ give a frame whose rapidity is *not* $\sqrt{a^2+b^2}$ but the value with $\cosh$ in place of the square root; the Euclidean hypotenuse is the small-rapidity approximation, and the difference is of order $a^2b^2$. The two-boost product is also not a pure boost: written in the polar decomposition $\tilde{\Lambda}_2\tilde{\Lambda}_1 = \tilde{\Lambda}_{\mathrm{boost}}\tilde{W}$ it contains the Wigner rotation $\tilde{W}$, which is the subject of the next section.

**Numerical check.** For $a = b = 1$ and $\theta = \pi/2$ the composition law gives $\cosh\rho = \cosh^2 1 = 2.38110$ and $\rho = 1.51337$, against the Euclidean hypotenuse $\sqrt{a^2+b^2} = 1.41421$; the two differ by $0.09916$, which is the gap of order $a^2b^2$ between the exact rule and the flat approximation. The composed four-velocity, computed by multiplying the two $4\times4$ boost matrices, has the same $\gamma$ as $\cosh\rho$ to machine precision.

## The Curvature of the Boost Connection

### The holonomy is the hyperbolic area

A boost is a point of velocity space, and a path of boosts is a path in it; the statement that a closed path of boosts need not be a closed path of frames is the statement that the connection has curvature, and the Wigner rotation is its holonomy. The holonomy has a closed geometric value.

**Proposition.** Let $\tilde{\Lambda}_1$ have rapidity $a$ along $\hat{\mathbf{n}}_1$ and $\tilde{\Lambda}_2$ rapidity $b$ along $\hat{\mathbf{n}}_2$, let $\rho$ be the rapidity of the composed frame, fixed by the composition law above, and let $\alpha$ be the angle of the Wigner rotation of the product $\tilde{\Lambda}_2\tilde{\Lambda}_1$. Then, in rapidity units,
$$
\alpha = \pi-(A+B+C) ,
$$
the angle defect of the geodesic triangle of velocity space whose three side lengths are $a$, $b$ and $\rho$; equivalently, since the curvature is $-1$, $\alpha$ is the **hyperbolic area** of that triangle. In physical units the angle is the area divided by $c^2$, $\alpha = A_{\mathrm{hyp}}/c^2$.

The triangle is the **rapidity triangle** of the loop: its sides are the three rapidities, and its existence is the triangle inequality of the geometry, $\rho<a+b$. The proposition says that the whole of the rotation produced by a closed path of boosts is measured by the hyperbolic area the three rapidities span, which is the Gauss–Bonnet theorem for the boost connection.

**Verified numerically.** The holonomy was computed from the $2\times2$ matrix model by the polar decomposition $\tilde{\Lambda}_2\tilde{\Lambda}_1 = HU$, $H$ Hermitian positive and $U$ unitary, with $\alpha = 2\arccos(\mathrm{tr}\,U/2)$, and compared with the angle defect of the triangle of sides $a,b,\rho$. The two agree to machine precision (largest discrepancy $2.4\times10^{-14}$ rad) over a grid of $a,b$ in $[0.5,2]$ and $\theta$ in $\{30^\circ,60^\circ,90^\circ,120^\circ\}$. The unitary part is a rotation about the normal to the plane of the loop, exactly along $\hat{\mathbf{z}}$ when the two boosts are along $\hat{\mathbf{x}}$ and $\hat{\mathbf{y}}$.

A sharpening of the companion article's reading is worth stating, because the triangle is not the one the eye first draws. The companion article places the vertices of the path at rapidities $(0,0)$, $(a,0)$ and $(a,b)$ and calls $\tfrac12 ab$ the enclosed area; that is the flat approximation, and it is the approximation to the **rapidity triangle** — the triangle whose sides are the three rapidities. The image of the path in velocity space is a different triangle. Its vertices are the rest point, the frame after the first boost, and the frame after the second, and its sides are $a$, $\rho$, and the length of the orbit of the first frame under the second boost; that last length is *not* the rapidity $b$ of the second boost, because a boost of rapidity $b$ moves a point that is already moving further than it moves the rest point. For $a = 0.7$, $b = 1.1$ and perpendicular boosts, the side in question is $1.3472$ where $b = 1.1$, and the area of the image triangle is $22.46849^\circ$ where the holonomy is $19.11370^\circ$ — the latter being exactly the defect of the rapidity triangle of sides $0.7$, $1.1$ and $\rho = 1.36975$. So the area that Gauss–Bonnet assigns to the holonomy is the area of the rapidity triangle, and it is that triangle, not the traced figure, that the area statement is about.

### The Euclidean area and the companion article's numbers

For small rapidities the defect has the expansion
$$
\alpha = \frac{ab}{2}-\frac{ab\,(a^2+b^2)}{24}+\cdots ,
$$
so the Euclidean area $\tfrac12 ab$ is the leading term and the hyperbolic area is smaller, by an amount of order $a^4$. The companion article on the Wigner rotation records the ratio $\alpha/(ab)$ at three small loops and observes it drifting *below* $\tfrac12$ without identifying the cause:

| $(a,b)$ | $\alpha/(ab)$ recorded | $\tfrac12-\tfrac{a^2+b^2}{24}$ |
|---|---|---|
| $(0.05,0.05)$ | $0.499792$ | $0.4997917$ |
| $(0.2,0.1)$ | $0.497921$ | $0.4979167$ |
| $(0.3,0.3)$ | $0.492514$ | $0.4925$ |

The drift is the angle defect: the recorded values agree with $\tfrac12-(a^2+b^2)/24$ to the accuracy of the recorded digits, the residual being the next order of the expansion. The Euclidean area of the loop is the flat approximation, and the deficit is the curvature of velocity space. The same expansion explains why the recorded values fall short of $\tfrac12$ monotonically in the loop size, and why the effect is invisible at $a = b\ll1$.

### Thomas precession as the rate form

For a particle whose velocity traces a path in velocity space — an accelerated particle — the holonomy accumulated along the path is a continuous rotation of the rest-frame spin, and its rate is Thomas precession,
$$
\dot{\boldsymbol{\Omega}}_{\mathrm{T}} = -\frac{\gamma-1}{v^2}\,\mathbf{v}\times\dot{\mathbf{v}} ,
$$
the infinitesimal form of the statement that the area swept out per unit time is the rotation accumulated per unit time. The rate form is derived in the companion article on the Wigner rotation; the present article supplies what the rate does not: the exact finite statement, and the identification of the accumulated angle with an area rather than with a Euclidean product of rapidities. In dimensions other than three the same structure is the statement that the symmetric space $SL(2,\mathbb{C})/SU(2)$ has rank one, so its curvature is a single number and every loop's holonomy is a single angle.

## The Light Cone Is the Boundary at Infinity

### $c$ is at infinite distance

The ball $|\mathbf{v}|<c$ is the whole of velocity space and its boundary is the light cone. The distance from any velocity to the boundary is infinite, because the distance from $\mathbf{v}$ to a boundary point is $\rho$ with $v = c\tanh(\rho/c)$, and $\rho\to\infty$ as $v\to c$. So the light cone is the **boundary at infinity** of velocity space, and it is not a part of it: a photon is not a velocity with a large value, it is a point at infinity, and the reason $c$ cannot be reached by composing velocities is the trigonometrical one that no finite arc length reaches the boundary.

The metric coefficient $\sinh^2(\rho/c)$ makes the circumference of the circle of radius $\rho$ grow exponentially, so velocity space opens so rapidly that the boundary is unreachable: the content of the statement that velocity space is *complete* as a Riemannian manifold while the ball of Euclidean geometry is not. A particle's rapidity can grow without bound while its velocity approaches $c$ asymptotically, and the energy grows as $\cosh\psi$ along the way; the divergence of the energy at $v = c$ is the infinite geodesic distance to the boundary.

### The zero divisors are the ideal points

The absolute of velocity space is the light cone, and in the algebra the light cone is the zero-divisor cone $N(\tilde{Q}) = 0$: the boundary points are exactly the elements the biquaternion algebra cannot invert. This is the reading the algebra adds to the classical account. The cross-ratio that defines the Cayley–Klein distance is built from the two boundary points of the chord, so the distance between two velocities is a cross-ratio taken against **zero divisors**; and the two ends of each chord are the two null directions of the two-plane through the origin that carries the chord, so the metric of velocity space is the measure of the velocity circle against the algebra's singular elements. That the ideal points are the singular elements is the algebraic form of the statement that the boundary of the geometry is the boundary of the algebra's invertibility, which is the thesis of the companion article on the zero-divisor cone.

## The Two Sectors

The geometry belongs to the material sector, and its curvature is measured in the informational one, which is worth separating.

The velocity hyperboloid is a quadric in $\mathbb{M}_-$, the material sector, where the four-velocities live; the distance $d$ between two velocities is a material quantity, computed from the biquaternion norm $N$ of two elements of $\mathbb{M}_-$. The boost rotor is Hermitian, an element of $\mathbb{M}_+$; the holonomy is unitary, an element of the rotation group inside $\mathbb{M}_-^{0}$; and the angle $\alpha$ is read off the trace of the unitary part, which is a statement about the informational sector's operator algebra. So the curvature of the boost connection is the one place in the relativity series where a geometric quantity of the material sector — an area — is literally equal to an operator-theoretic quantity of the informational sector — a rotation angle. The equality is the content of the statement that the two sectors are the two signatures of the same form, and the Gauss–Bonnet theorem is the bridge between them.

For a spin the area statement has the operational reading of the companion article: a transverse loop of boosts imprints on the spin a rotation of angle equal to the area, and the entropy it can imprint is $h((1+\cos\alpha)/2)$, so the hyperbolic area is a bound on the information a closed path of frame changes can carry to the spin.

## What the Framework Supplies and What It Transcribes

**What the framework supplies.** The velocity space is not imported: it is the quadric $N(\tilde{U}) = -c^2$ in the material sector, and the metric on it is computed from the biquaternion norm in the algebra's own coordinates, with the Weierstrass parametrisation the algebra's parametrisation of the quadric. The boundary at infinity is the zero-divisor cone, which the algebra carries as the set of non-invertible elements, so the boundary of the geometry and the boundary of invertibility are the same set. The holonomy is the unitary part of the polar decomposition of a product of rotors, computed with the rotor conjugation and the trace, and the statement that its angle is the hyperbolic area is a statement about the algebra's own multiplication. And the $c\mapsto ic$ interchange of the spherical and hyperbolic representations is, in the algebra, the interchange of the two real directions of the trace-free subalgebra — the compact rotation directions and the hyperbolic boost directions — which is a single algebraic fact rather than a formal substitution.

**What it transcribes.** The metric of velocity space, the Cayley–Klein distance, the velocity-addition law as hyperbolic trigonometry, and the identification of the Wigner rotation with the curvature of the boost connection are all classical: they are Varićak's and Sommerfeld's hyperbolic reading of relativity, developed in the modern literature as the hyperbolic geometry of velocity space and as the gyrogroup formalism. The framework does not derive them; it re-expresses them in one algebra, and it supplies the sector reading of the boundary and the exact area statement, which the classical account gives only in the rate form.

**What is not claimed.** No claim is made that velocity space is a *spacetime*: it is an abstract Riemannian manifold of curvature $-1/c^2$ whose points are the velocities of a given spacetime, and it must not be confused with the hyperbolic geometries of *curved spacetime*, which are Riemannian or Lorentzian geometries of the spacetime itself. The identification is of the velocity space, not of the space of events. Nor is the holonomy-area statement claimed to be new as hyperbolic geometry; it is claimed to be the exact form of the companion article's numerical observation, and it has been verified numerically here rather than proved from the algebra.

**Open questions.** Whether the hyperbolic area statement has a direct derivation inside the algebra, without passing through the symmetric space and Gauss–Bonnet; whether the same geometry organises the mass shells of different masses into a foliation of $\mathbb{H}^3$ with a natural meaning; and whether the map from the rapidity triangle to the spin entropy of the companion article can be made into an exact channel, are left open.

## Summary

The velocity space of a massive particle is a hyperbolic three-space of curvature $-1/c^2$. Its carrying manifold is the quadric $N(\tilde{U}) = -c^2$ in the material sector, the future sheet of the mass-shell hyperboloid; parametrised in Weierstrass coordinates $\tilde{U} = c(\sinh(\rho/c)\hat{\mathbf{u}}+i\cosh(\rho/c)e_0)$, the geodesic distance $\rho$ is $c$ times the rapidity and the metric is $ds^2 = d\rho^2+c^2\sinh^2(\rho/c)d\Omega^2$. In the velocity coordinates the metric is the Beltrami–Klein metric $ds^2 = c^2[(c^2-\mathbf{v}^2)|d\mathbf{v}|^2+(\mathbf{v}\cdot d\mathbf{v})^2]/(c^2-\mathbf{v}^2)^2$, the geodesics are the straight chords of the ball $|\mathbf{v}|<c$, and the distance between two velocities is the relative rapidity, $\cosh(d/c) = \gamma_1\gamma_2(1-\mathbf{v}_1\cdot\mathbf{v}_2/c^2)$, equivalently the Cayley–Klein cross-ratio against the two lightlike ends of the chord.

The composition of two boosts is the trigonometry of geodesic triangles. The rapidity is additive on a line and Einstein's addition law is the geodesic parametrisation; the relative-velocity formula is the hyperbolic law of cosines for the triangle of the three frames; and the composition law of two boosts of rapidities $a,b$ at an angle $\theta$ is the spherical-type relation $\cosh\rho = \cosh a\cosh b+\cos\theta\sinh a\sinh b$, the two laws being exchanged by $c\mapsto ic$, the Sommerfeld representation on a sphere of imaginary radius. The Wigner rotation of the product is the holonomy of the boost connection, and its angle is the hyperbolic area of the geodesic triangle whose sides are the three rapidities of the loop; the Euclidean area $\tfrac12 ab$ is the leading term and the correction is $-\tfrac{1}{24}ab(a^2+b^2)$, which reproduces the drift recorded in the companion article on the Wigner rotation. The light cone is the boundary at infinity — the absolute of the Cayley–Klein model — at infinite geodesic distance from every velocity while the velocity is bounded by $c$, and in the algebra it is the zero-divisor cone, so the ideal points of the geometry are the elements the algebra cannot invert. The area statement is the one place where a geometric quantity of the material sector equals an operator quantity of the informational sector, because the curvature of the boost connection is an area and the holonomy is a rotation angle.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde{U} = \gamma(ic\,e_0+\mathbf{v})$ | Four-velocity, $N(\tilde{U}) = -c^2$, future sheet of the hyperboloid in $\mathbb{M}_-$ |
| $\rho$ | Geodesic distance in velocity space from rest; $\rho = c\,\mathrm{artanh}(v/c)$ |
| $\psi = \rho/c$ | Rapidity; additive along a line |
| $\tilde{U} = c(\sinh\frac{\rho}{c}\hat{\mathbf{u}}+i\cosh\frac{\rho}{c}e_0)$ | Weierstrass coordinates of the velocity hyperboloid |
| $ds^2 = d\rho^2+c^2\sinh^2\frac{\rho}{c}\,d\Omega^2$ | Metric of velocity space, curvature $-1/c^2$ |
| $ds^2 = c^2\frac{(c^2-\mathbf{v}^2)\lvert d\mathbf{v}\rvert^2+(\mathbf{v}\cdot d\mathbf{v})^2}{(c^2-\mathbf{v}^2)^2}$ | The same metric in the velocity (Beltrami–Klein) coordinates |
| $\cosh\frac{d}{c} = \gamma_1\gamma_2(1-\frac{\mathbf{v}_1\cdot\mathbf{v}_2}{c^2})$ | Distance between two velocities = relative rapidity |
| $d = \frac{c}{2}\lvert\log\frac{\lvert\mathbf{v}_1a\rvert\lvert\mathbf{v}_2b\rvert}{\lvert\mathbf{v}_1b\rvert\lvert\mathbf{v}_2a\rvert}\rvert$ | The same as a Cayley–Klein cross-ratio with the boundary |
| $v_{\mathrm{tot}} = c\tanh(\psi_1+\psi_2)$ | Einstein addition, as the geodesic parametrisation |
| $\cosh\rho = \cosh a\cosh b+\cos\theta\sinh a\sinh b$ | Composition law of two boosts (spherical type) |
| $\cosh\frac{d}{c} = \cosh\psi_1\cosh\psi_2-\cos\theta\sinh\psi_1\sinh\psi_2$ | Relative velocity (hyperbolic law of cosines) |
| $c\mapsto ic$ | Sommerfeld interchange of the hyperbolic and spherical representations |
| $\alpha = \pi-(A+B+C) = A_{\mathrm{hyp}}/c^2$ | Wigner angle = hyperbolic area of the rapidity triangle |
| $\alpha = \frac{ab}{2}-\frac{ab(a^2+b^2)}{24}+\cdots$ | Small-loop expansion; the Euclidean area is the leading term |
| $\lvert\mathbf{v}\rvert = c$, $N(\tilde{Q}) = 0$ | Boundary at infinity = light cone = zero-divisor cone |

## Further Reading

- Vladimir Varićak, "Über die nichteuklidische Interpretation der Relativtheorie", *Jahresbericht der Deutschen Mathematiker-Vereinigung* **21** (1912) 103–127, for the Lobachevsky interpretation of the relative velocity and the original hyperbolic reading of the theory.
- Arnold Sommerfeld, "Über die Zusammensetzung der Geschwindigkeiten in der Relativtheorie", *Physikalische Zeitschrift* **10** (1909) 826–829, for the composition of velocities on a sphere of imaginary radius.
- John Frederick Barrett, "Minkowski space-time and hyperbolic geometry", MASSEE International Congress on Mathematics MICOM-2015, Athens (September 2015), for the differential Minkowski space, the hyperboloid in velocity space $V_t^2-V_x^2-V_y^2-V_z^2 = c^2$, the Cayley–Klein distance as the inner product of two four-velocities, the Weierstrass coordinates, the Beltrami–Klein representation, the statement that the radius of negative curvature is $c$ and that the spherical and hyperbolic metrics are interchanged by substituting $iR$ for $R$, and the history (Wick, Pauli, Carathéodory, Sommerfeld, Varićak) — the immediate source for the account followed here.
- John Frederick Barrett, *The Hyperbolic Theory of Special Relativity*, monograph (Southampton, 2006; revised 2010 and 2019), arXiv:1102.0462, for the fuller development of the same material, including the Thomas precession and the hyperbolic area formula in its mathematical appendix; its epigraph is Borel's, quoted above.
- Abraham A. Ungar, *Analytic Hyperbolic Geometry: Mathematical Foundations and Applications* (World Scientific, 2005), and *Analytic Hyperbolic Geometry and Albert Einstein's Special Theory of Relativity* (World Scientific, 2008), for the gyrogroup formalism and the Thomas precession as the holonomy of velocity space.
- John A. Rhodes and Mark D. Semon, "Relativistic velocity space, Wigner rotation, and Thomas precession", *American Journal of Physics* **72** (2004) 943–960, arXiv:gr-qc/0501070, for the velocity space as a curved manifold and the Wigner rotation as its curvature.
- Domenico Giulini, "Algebraic and geometric structures in special relativity", *Lecture Notes in Physics* **702** (2006) 45–111, arXiv:math-ph/0602018, for the boost manifold as a symmetric space.
- John Stillwell, *Sources of Hyperbolic Geometry* (American Mathematical Society and London Mathematical Society, 1996), for the original papers of Beltrami and Klein and the Cayley–Klein construction.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the hyperboloid model, the Weierstrass coordinates and Gauss–Bonnet in hyperbolic space.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor calculus of boosts and the composition of rotations.
- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* **40** (1939) 149–204, for the little group and the original Wigner rotation.
- L. H. Thomas, "The kinematics of an electron with an axis", *Philosophical Magazine* **3** (1927) 1–22, for the precession of an accelerated spin and its rate form.
