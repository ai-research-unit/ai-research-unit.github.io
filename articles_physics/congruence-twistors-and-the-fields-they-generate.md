# __Congruence Twistors and the Fields They Generate__

## Introduction

The corpus holds the three pieces of one construction, in three different articles, and never joins them. *Twistor Theory and Biquaternions* states the incidence relation $\omega=i\,x\pi$ and the null quadric. *Null Electromagnetic Fields and the Shear-Free Congruence* states that a null field's principal direction is geodesic and shear-free. *The Algebrodynamical Programme* states that the equation of the shear-free congruence is solved by an arbitrary holomorphic function $\Pi$ of the twistor arguments, and that Maxwell, Yang–Mills and the effective geometry all descend from that one function.

This article joins them. The join is a single geometric statement and a single algebraic statement. Geometrically, **a congruence is a two-surface in projective twistor space, a spacetime point is a line in that space, and the congruence's spinor at the point is the intersection of the two**. Algebraically, every function of the twistor components satisfies one pair of first-order relations, and that pair is at once the complex eikonal and the constraint that the programme derives for its gauge parameter, with the wave equation following as well for the functions of $G$.

The source is Kassandrov and Rizcallah, *Maxwell, Yang–Mills, Weyl and eikonal fields defined by any null shear-free congruence* (arXiv:1612.06718, 2016). The article records the twistor side of that paper. The field algebra it belongs to — the nonlinear Cauchy–Riemann conditions, the generating system, the weak self-duality, the charge quantisation, the particle reading — is recorded once in *The Algebrodynamical Programme* and is not restated here; where the two overlap, the reader is sent there.

The overlap is real and is stated at the outset so that the division is visible. The programme article already records the two first-order relations for the principal ratio, and already draws from them the complex eikonal, the wave equation and the harmonicity of $\ln G$, with a recomputation on one explicit solution of the quadratic Kerr equation. It records the electromagnetic field as the second derivatives of $\ln G$ in the source's component assignment, and the representation of that field through the derivatives of $\Pi$ alone. It records the coincidence of the singular loci. **What this article adds is five things and no more.**

- The relations are shown to hold for an arbitrary function of *all three* twistor components and not only of $G$, which is what makes the gauge group close and the rank statement work.
- That pair is identified with the constraint the source imposes on its rescaling parameter, so that the gauge condition and the eikonal are one equation.
- The reach of the pair is mapped: the eikonal holds for every twistor function, the wave equation only for the functions of $G$, and the difference is computed rather than asserted.
- The gauge group is described as a group acting on a surface, with the projective twistor space as its orbit set.
- The paper's two other field statements — the spinor inside the potential and the closed-form Yang–Mills triplet — are recorded, neither being anywhere in the corpus.

The recomputations are these, and each is reported where it is used. The null-twistor identity for a Hermitian coordinate matrix, on a hundred random Hermitian matrices. The pair of first-order relations and the eikonal, **symbolically, for an arbitrary generating function**, with vanishing residual — the programme article's check was numeric and on one quadratic generator, so the symbolic form is a strengthening rather than a repetition. The rank of the twistor field's Jacobian, on a hundred random complex points for each of three generating functions — quadratic, cubic and transcendental — checking that every three-by-three minor vanishes and that some two-by-two minor does not. The triplet's modulus identity, on a hundred random complex pairs. And the tangency condition of the static Kerr generator, which reduces to $r_*^2=0$ exactly.

Two claims are quoted and not recomputed, because they belong to the programme's own machinery rather than to the twistor geometry: that the field built from the second derivatives of $\ln G$ satisfies the source-free Maxwell equations, and the explicit representation of that field through the derivatives of $\Pi$ alone. Both are recorded in *The Algebrodynamical Programme*. Of the first, only the harmonicity of $\Lambda$ that carries it was checked here; the Maxwell equations themselves, and the whole of the second claim, are quoted and not re-derived, because the field-theoretic content of either is not what this article is about.

The conventions are those of the read-list articles and of the companion mathematics article *The Two-Sided Derivative over the Biquaternion Algebra*, which owns the coordinate chart. The complexified Minkowski coordinates are the four entries of the matrix

$$
Z=\begin{pmatrix}\upsilon & w\\ p & v\end{pmatrix},
$$

with $\upsilon,v,w,p$ the complex coordinates and $z_0=\tfrac12(\upsilon+v)$, $z_3=\tfrac12(\upsilon-v)$, $z_1=\tfrac12(w+p)$, $z_2=\tfrac{i}{2}(w-p)$; on the real slice $\upsilon=t'+z$, $v=t'-z$, $w=x-iy$, $p=x+iy=\bar w$. The d'Alembertian is $\Box=4(\partial^2/\partial\upsilon\,\partial v-\partial^2/\partial w\,\partial p)$ and the complex eikonal is

$$
\frac{\partial\Sigma}{\partial\upsilon}\frac{\partial\Sigma}{\partial v}=\frac{\partial\Sigma}{\partial w}\frac{\partial\Sigma}{\partial p}.
$$

The principal spinor is $\xi=(\xi_0,\xi_1)$, its ratio is $G=\xi_1/\xi_0$, and the gauge $\xi_0=1$ is used wherever a component is written out. Every partial derivative is written with the variable named after it, $\partial G/\partial\upsilon$, in the spelling the conventions article requires, and the two companion articles are written in the same spelling. The two twistor components attached to $G$ are

$$
\kappa_0=wG+\upsilon,\qquad \kappa_1=vG+p ,
$$

and the generating function is an arbitrary holomorphic $\Pi(G,\kappa_0,\kappa_1)$, with $P=\partial\Pi/\partial G$.

## The Coordinate Matrix and Its Two Columns

A point of complexified Minkowski space is a two-by-two complex matrix $Z$, and the incidence relation

$$
\tau=Z\xi,\qquad \tau_A=\sum_B Z_{AB}\,\xi_B ,
$$

attaches to a spinor $\xi$ a second spinor $\tau$. Read as a map, $\xi\mapsto(\xi,Z\xi)$ is complex linear from $\mathbb{C}^2$ into $\mathbb{C}^4$, its image is two-dimensional, and the pair $(\xi,\tau)$ is the **twistor** of the point. *Twistor Theory and Biquaternions* writes the same relation as $\omega=i\,x\pi$, with $x$ the Hermitian coordinate matrix and the $i$ the complex unit of twistor space; this article follows the source and writes $Z$, absorbing that $i$ into the coordinates, so that the Hermitian character of $Z$ on the real slice is simply the reality of $t',x,y,z$. Two facts follow at once, and both are used below.

**The image is a plane, so a spacetime point is a plane in twistor space.** Conversely every two-plane of $\mathbb{C}^4$ that is the graph of a linear map is the plane of exactly one point: the four entries of $Z$ are read off the plane, and the map between points and planes is a bijection. Projectively the plane becomes a **line** in $\mathbb{PT}$, and the correspondence is the classical one — a point of spacetime is a line, a point of twistor space is a two-surface.

**On the real slice the plane is null.** A twistor is null when $\tau^{*}\xi-\xi^{*}\tau=0$. With $Z$ Hermitian this holds identically, because

$$
\tau^{*}\xi=\xi^{*}Z^{*}\xi=\xi^{*}Z\xi=\xi^{*}\tau ,
$$

the middle step being the Hermiticity. The identity was checked on a hundred random Hermitian matrices, with a worst relative residual of $1.0\times10^{-15}$. So the planes that represent real spacetime points lie inside the null quadric of twistor space, and the correspondence restricted to the real slice is a correspondence between real points and null lines. **The null quadric of twistor space and the zero-divisor cone of the algebra are the same cone**, which is the agreement recorded in *Twistor Theory and Biquaternions*; what the computation above adds is that the equivalence is not merely at the level of the defining equations but holds for the full incidence data.

## The Twistor Surface

Fix a holomorphic function $\Pi$ of the three projective components. The equation

$$
\Pi(G,\kappa_0,\kappa_1)=0
$$

defines a **two-complex-dimensional surface** $S$ in $\mathbb{PT}$ — three projective coordinates, one equation — and the congruence's spinor at the point $x$ is the intersection of $S$ with the line $L_x$ attached to $x$. That single sentence is the geometric content of the whole construction, and everything else in this article is a consequence of it.

**The intersection explains the multivaluedness.** Restricted to the line, $\Pi$ becomes a polynomial in $G$ whose degree is $\Pi$'s total degree in its three arguments, so the line meets the surface in that many points, counted with multiplicity. A quadratic generator gives two roots, a cubic three; the corpus's *The Algebrodynamical Programme* records the resulting multivaluedness and the programme's insistence that it is required rather than tolerated, together with the topological route to charge quantisation that it supplies. The addition here is the reason: **the multivaluedness is Bézout's theorem.** It is not a defect of the eikonal equation and not a failure of the ansatz; it is the count of intersections of a line with a surface, and it disappears only when the surface is a plane.

**The singular locus is a tangency.** When the line is tangent to the surface the roots coincide, the implicit resolution of $\Pi=0$ for $G$ fails, and $P=\partial\Pi/\partial G$ vanishes beside $\Pi$. This is the condition the programme uses as its singular set, and in the twistor picture it is one thing only: *the set of spacetime points whose line is tangent to the twistor surface*. The point-like, string-like and surface-like singular sets of the programme's catalogue are then the various ways a two-surface can be touched by a family of lines.

## The Pair of Relations

The algebraic content of the construction is one pair of equations, and it is worth isolating because two separate results of the source follow from it, with a third that follows only in part. The programme article records the pair for the principal ratio and draws the eikonal and the wave equation from it; what is done here is to derive the pair once for an arbitrary generating function, extend it to every twistor function, and identify it with the gauge constraint.

**The relations.** For the principal ratio $G$ obtained from any $\Pi$,

$$
\frac{\partial G}{\partial w}=G\,\frac{\partial G}{\partial\upsilon},
\qquad
\frac{\partial G}{\partial v}=G\,\frac{\partial G}{\partial p}.
$$

**Where they come from, and why they hold for every generating function.** Differentiating $\Pi(G,\kappa_0,\kappa_1)=0$ at fixed coordinates, and using $\partial\Pi/\partial\upsilon=\partial\Pi/\partial\kappa_0$, $\partial\Pi/\partial w=G\,\partial\Pi/\partial\kappa_0$, $\partial\Pi/\partial p=\partial\Pi/\partial\kappa_1$ and $\partial\Pi/\partial v=G\,\partial\Pi/\partial\kappa_1$, the implicit derivatives are

$$
\frac{\partial G}{\partial\upsilon}=-\frac{1}{P}\frac{\partial\Pi}{\partial\kappa_0},\qquad
\frac{\partial G}{\partial w}=-\frac{G}{P}\frac{\partial\Pi}{\partial\kappa_0},\qquad
\frac{\partial G}{\partial v}=-\frac{G}{P}\frac{\partial\Pi}{\partial\kappa_1},\qquad
\frac{\partial G}{\partial p}=-\frac{1}{P}\frac{\partial\Pi}{\partial\kappa_1},
$$

and the two relations are read off by inspection. They are therefore not properties of a solution but properties of the **ansatz**: no generating function is special, and no solution has to be exhibited to know that they hold. Verified symbolically with the three partials of $\Pi$ kept as free symbols, the residuals are exactly zero, and they are zero for the same reason in every degree.

**Every twistor function obeys them.** Let $\lambda$ be any differentiable function of the three twistor components, $\lambda=\lambda(G,\kappa_0,\kappa_1)$. Since $\partial\kappa_0/\partial\upsilon=1+w\,\partial G/\partial\upsilon$, $\partial\kappa_0/\partial w=G+w\,\partial G/\partial w$, and similarly in the other column, the relations for $G$ give

$$
\frac{\partial\kappa_0}{\partial w}=G\,\frac{\partial\kappa_0}{\partial\upsilon},
\qquad
\frac{\partial\kappa_1}{\partial w}=G\,\frac{\partial\kappa_1}{\partial\upsilon},
\qquad
\frac{\partial\kappa_0}{\partial v}=G\,\frac{\partial\kappa_0}{\partial p},
\qquad
\frac{\partial\kappa_1}{\partial v}=G\,\frac{\partial\kappa_1}{\partial p},
$$

and the chain rule carries the pair to $\lambda$ unchanged,

$$
\frac{\partial\lambda}{\partial w}=G\,\frac{\partial\lambda}{\partial\upsilon},
\qquad
\frac{\partial\lambda}{\partial v}=G\,\frac{\partial\lambda}{\partial p}.
$$

This was verified symbolically for an arbitrary $\lambda$, with its three partials free, and the residual is zero.

**Two consequences, and they differ.** Multiply the pair:

$$
\frac{\partial\lambda}{\partial\upsilon}\frac{\partial\lambda}{\partial v}
=\frac{\partial\lambda}{\partial w}\frac{\partial\lambda}{\partial p},
$$

which is the complex eikonal, and it holds for **every** function of the twistor. Cross-differentiate the pair instead. Differentiating $\partial\lambda/\partial w=G\,\partial\lambda/\partial\upsilon$ in $v$ and $\partial\lambda/\partial v=G\,\partial\lambda/\partial p$ in $w$, and equating the two mixed derivatives, gives

$$
\frac{\partial G}{\partial v}\frac{\partial\lambda}{\partial\upsilon}+G\,\frac{\partial^2\lambda}{\partial v\,\partial\upsilon}
=\frac{\partial G}{\partial w}\frac{\partial\lambda}{\partial p}+G\,\frac{\partial^2\lambda}{\partial w\,\partial p},
\qquad\text{hence}\qquad
\Box\lambda=4\left(\frac{\partial G}{\partial\upsilon}\frac{\partial\lambda}{\partial p}-\frac{\partial G}{\partial p}\frac{\partial\lambda}{\partial\upsilon}\right),
$$

on using $\partial G/\partial v=G\,\partial G/\partial p$ and $\partial G/\partial w=G\,\partial G/\partial\upsilon$ and dividing by $G$.

**The wave equation is therefore not a consequence of the pair alone, and this is the one place where the article must part company with a natural guess.** The bracket of the last display vanishes identically when $\lambda$ depends on $G$ alone, because then $\partial\lambda/\partial p=(d\lambda/dG)\,\partial G/\partial p$ and $\partial\lambda/\partial\upsilon=(d\lambda/dG)\,\partial G/\partial\upsilon$; it does not vanish for a general twistor function. At $\lambda=G$ the display reads $\Box G=0$, which is the wave equation the source derives, and that is the sense in which the source's statement is about $G$. Checked numerically on the quadratic generator at forty digits with warm-started Newton continuation: $\Box G$ and $\Box\ln G$ came out at $5\times10^{-14}$ and $6\times10^{-14}$ against a second-difference floor of order $h^2=10^{-12}$, while $\Box\kappa_0$ and $\Box\kappa_1$ came out at $0.16$ and $0.31$; and the identity above reproduced the values of $\Box\kappa_0$ and $\Box\kappa_1$ to a relative $6\times10^{-13}$.

So the pair gives two things of different reach. **The eikonal holds for all twistor functions** — every one of them is a null gradient — and **the wave equation holds for the functions of $G$ alone**, which is exactly the boundary the programme article draws when it says that every $C^2$ function of $G$ is harmonic on the solutions. The asymmetry is what the field construction needs and no more: the field is built from $\Lambda=\ln G$, a function of $G$, so harmonicity is available where it is used, and the gauge parameter, which is a general twistor function, is required only to be null.

**The same pair is the gauge constraint.** This is the observation that ties the algebra to the geometry. The programme requires its rescaling parameter to depend on the coordinates only through the twistor, and the differential form of that requirement is that $\alpha$ is constant along each ray: the principal spinor $\xi=(1,G)$ contracted into the gradient of $\alpha$ vanishes. In components that condition is

$$
-G\,\frac{\partial\alpha}{\partial\upsilon}+\frac{\partial\alpha}{\partial w}=0,
\qquad
-G\,\frac{\partial\alpha}{\partial p}+\frac{\partial\alpha}{\partial v}=0,
$$

which is the pair again. **The condition that a rescaling be a symmetry and the condition that a function be a solution of the complex eikonal are the same equation**, and its solutions are exactly the functions of the twistor. Harmonicity, by the preceding section, is a further requirement, met when the twistor function depends on $G$ alone. This is why the gauge group of the next section is what it is, and it is the sharpest single statement in the paper.

## Two Independent Components

A four-component twistor whose components are functions of four coordinates could depend on all four. It does not: exactly two of its components are functionally independent, and the count is what makes the twistor field a two-surface rather than a four-dimensional spread.

The statement is that the map $x\mapsto(G,\kappa_0,\kappa_1)$ has a Jacobian of rank exactly two, so that all three-by-three minors vanish and some two-by-two minor does not. This was checked numerically at forty working digits, on a hundred random complex points for each of three generating functions — a quadratic, a cubic, and a transcendental one — with the derivatives taken in closed form from the implicit expressions above. **The largest three-by-three minor, scaled by the cube of the Jacobian's largest entry, was $2.9\times10^{-41}$, $1.4\times10^{-41}$ and $2.0\times10^{-41}$ for the three families; the smallest of the largest two-by-two minors, scaled by the square of the same entry, was $0.399$, $0.515$, $0.122$.** The vanishing minors sit at the rounding floor of forty-digit arithmetic and the non-vanishing ones at $O(0.1)$, so the rank is two with forty orders of margin.

**Physical interpretation.** Rank two is the statement that the twistor field is a surface, and a surface is what the line has to meet. The count of components, the count of intersections, and the count of dimensions of $S$ are the same count seen three ways, and this is why the construction is rigid: the data are a surface, and a surface is fixed by one holomorphic function of three arguments, which is where the freedom sits and where it stops.

## The Weakened Gauge Group

A rescaling of the spinor $\xi\mapsto\alpha(x)\xi$ is not a symmetry of the congruence equations unless $\alpha$ is restricted, and the restriction is the pair of the preceding section. The source's reading is that the symmetry group is therefore not the full group of complex functions but the group of functions **of the twistor**,

$$
\xi\mapsto\alpha(T)\,\xi,\qquad \tau\mapsto\alpha(T)\,\tau,\qquad T\mapsto\alpha(T)\,T .
$$

**It is a group, and the argument is the rank statement.** Composition of two such rescalings is multiplication of two functions of $T$, hence of the same type; associativity is inherited; and the inverse exists because $T$ has only two functionally independent components, so the two independent components of the image determine those of the argument, and $\alpha^{-1}$ read on the image is again a function of the twistor. The last step is exactly where the rank-two result is used, and without it the construction would give a semigroup.

**The orbits are the projective twistors, and this is the point.** Since $\alpha$ is a function of $T$ and not of $x$, the ratio of any two twistor components is invariant, and two twistors related by a rescaling differ by nothing the geometry can see: the quotient by the group is the projective twistor space $\mathbb{PT}$. The corpus's twistor article records that the standard projective structure comes from the full $\mathbb{C}^{\times}$ action on the four components. Here the projective structure is **derived** instead: it is the orbit set of the symmetry group that the congruence actually has, and the group is a proper subgroup of the naive one. A rescaling with a parameter that is not a twistor function is not a symmetry, and the source states this explicitly.

**The potential shifts, and the field does not.** The trace of the matrix one-form $C\,dZ$ transforms as

$$
C\mapsto C+d\ln\alpha ,
$$

which is the transformation of an electromagnetic potential under an abelian gauge change, and the two-form $F=dC$ is invariant because $d\ln\alpha$ is closed. The invariance is thus exact and does not depend on the parameter being a twistor function; what depends on it is that the transformation is a symmetry of the *primary* system at all, and that the shift is a gradient of a function which the congruence itself defines.

**Physical interpretation.** The corpus's gauge articles take the gauge principle as a postulate: a symmetry is demanded, a connection is introduced to make a derivative covariant, and the field strength is the curvature. Here the order is reversed. The symmetry is a residual freedom of an over-determined system; the parameter is constrained by the system's own solution space; the connection is not introduced but read off; and the field strength's invariance is automatic. Whether that is an advance or a bookkeeping change is the judgement the corpus does not make, and the same reversal is stated in *The Algebrodynamical Programme* for the Maxwell and Yang–Mills equations.

## The Three Fields from One Function

Three distinct field equations hold on the solutions of the congruence equation, and all three are read from the same $\Pi$. The electromagnetic and Yang–Mills statements are recorded in *The Algebrodynamical Programme* and are repeated here only in the form the twistor makes available; the spinor statement is not recorded there and is the reason this section exists.

### The Electromagnetic Field

Let $\Lambda=\ln G$. It is a function of the single twistor component $G$, so it satisfies the pair, the eikonal and the wave equation, by the argument of the section above. The programme article writes the three independent components of the antiself-dual field as the second derivatives of $\Lambda$,

$$
F_{00}=\frac{\partial^2\Lambda}{\partial\upsilon\,\partial p},
\qquad
F_{01}=\frac{\partial^2\Lambda}{\partial w\,\partial p},
\qquad
F_{11}=\frac{\partial^2\Lambda}{\partial v\,\partial w},
$$

and the Maxwell equations then hold for it because $\Lambda$ is harmonic. That was checked directly: with $G$ solved by Newton continuation at forty digits and the derivatives taken by central differences, the eikonal residual of $\Lambda$ was $6.0\times10^{-16}$ and $5.7\times10^{-23}$ for the quadratic and transcendental generators, and the mixed derivative $\partial^2\Lambda/\partial\upsilon\,\partial v$ agreed with $\partial^2\Lambda/\partial w\,\partial p$ to twelve digits, which is $\Box\Lambda=0$ written out.

**The 2016 paper writes the same field as the second derivatives of $G$ itself.** Its three components are

$$
E_+=\frac{\partial^2G}{\partial\upsilon^2},
\qquad
E_3=-\frac{\partial^2G}{\partial\upsilon\,\partial p},
\qquad
E_-=-\frac{\partial^2G}{\partial p^2},
$$

which are $\partial\varphi_0/\partial\upsilon$, $-\partial\varphi_0/\partial p$ and $-\partial\varphi_1/\partial p$ in the surviving components $\varphi_0,\varphi_1$ of the next subsection, and the homogeneous Maxwell equations hold for them on the congruence by the wave equation for $G$. The two assignments are not the same components — $\partial\ln G=\partial G/G$ leaves behind a term quadratic in the first derivatives — and the article keeps them apart instead of presenting one as the other. What the two share is the singular locus, not the normalisation.

**The sharpest form of the result is the source's.** The field can be written through the derivatives of $\Pi$ alone,

$$
F_{AB}=\frac{1}{P}\,\Pi_{AB}-\frac{1}{P}\,\frac{d}{dG}\left(\frac{\Pi_A\Pi_B}{P}\right),
$$

with $\Pi_A$ and $\Pi_{AB}$ the first and second derivatives of $\Pi$ in its two twistor arguments and $P=d\Pi/dG$, in the companion article's notation for these derivatives, so that **the field of a congruence is computed from the generating function without ever solving the Kerr equation for $G$**. The corpus records this formula in *The Algebrodynamical Programme* and does not re-derive it; what this article adds is the reading of why it can exist at all. The field is a second derivative of a function of the twistor, the twistor is constrained to a surface, and a function on a surface has its derivatives fixed by the surface's defining equation — which is exactly what a formula in $\Pi$ and its derivatives expresses.

### The Spinor inside the Potential

This is the part of the paper the corpus does not otherwise have, and it is the reason the construction reaches the fermionic sector at all.

The potential is not a four-vector with something added to it. It is the array $\Phi_{B'A}$ of the source's (13), built from the spinor by $\Phi_{B'A}=\iota^{A}\nabla_{AA'}\xi_{B'}$ with a conjugate spinor $\iota$ normalised by $\xi_{A'}\iota^{A}=1$, and its two indices are of different kinds: by the transformation law (10), $\Phi\mapsto\bar L^{+}\Phi\bar L$, the group acts by $\bar L^{+}$ on the primed index and by $\bar L$ on the unprimed one. The object carries one primed and one unprimed spinor index, and fixing either index leaves a two-component spinor.

**In the gauge $\xi_{0'}=1$ half of it vanishes, and the reason is (13).** (The source writes the spinor with a primed index, $\xi_{A'}$; this is this article's $\xi=(1,G)$, so the gauge is the $\xi_0=1$ used above, and only the spelling differs.) There $\Phi_{0'A}=\iota^{A}\nabla_{AA'}\xi_{0'}$ is the derivative of the constant $\xi_{0'}=1$ and therefore zero, so the array is

$$
\begin{pmatrix}\Phi_{0'0} & \Phi_{0'1}\\ \Phi_{1'0} & \Phi_{1'1}\end{pmatrix}
=\begin{pmatrix}0 & 0\\ \varphi_0 & \varphi_1\end{pmatrix},
\qquad
\varphi_0=\frac{\partial\ln G}{\partial w}=\frac{\partial G}{\partial\upsilon},
\qquad
\varphi_1=\frac{\partial\ln G}{\partial v}=\frac{\partial G}{\partial p},
$$

the second equality in each being the pair of relations. **Two of the four components of the potential are zero by the choice of gauge, and the two that remain form a chiral two-spinor.** The vanishing is not an extra assumption: it is what the projective freedom $\xi\mapsto\alpha(T)\xi$ is spent on, and the source draws it from (13) and not from a postulate about the potential.

**The surviving pair satisfies the massless Weyl equation, and its content is the wave equation for $G$.** The source writes it as $\nabla_{AB'}\varphi^{A}=0$, whose two component equations are

$$
\frac{\partial\varphi_0}{\partial p}=\frac{\partial\varphi_1}{\partial\upsilon},
\qquad
\frac{\partial\varphi_0}{\partial v}=\frac{\partial\varphi_1}{\partial w},
$$

where $p$ is the coordinate $\bar w$ of this article's chart, not the twistor coordinate of the same name. Substituting the components, the first reads $\partial^2G/\partial\upsilon\,\partial p=\partial^2G/\partial p\,\partial\upsilon$ and is an identity of mixed partials; the second reads $\partial^2G/\partial\upsilon\,\partial v=\partial^2G/\partial w\,\partial p$ and is $\Box G=0$. So the pair carries the wave equation for $G$ beside an identity, and **it adds no equation of its own**: the Weyl relations hold because $G$ is null and harmonic, which is what the pair of the earlier section supplies. The source states the two equations as equivalent to the self-duality conditions together with the inhomogeneous Lorentz condition, which is what the first-order pair already encodes.

**What that leaves is nonetheless the substantive point.** A two-component spinor field, obeying the relations that a massless chiral fermion's field obeys, is what the complex four-potential becomes once its gauge freedom is spent, with no Dirac equation and no gamma matrices anywhere in the derivation. The potential is bigger than the electromagnetic field it carries, and the extra part is not gauge — it is a spinor. What the construction does not supply is a reason for the spinor to have a mass or to obey a massive equation, and the source claims neither.

**Physical interpretation.** The corpus derives its fermions from the Dirac equation and its bosons from the gauge principle, and treats the two as separate imports. Here one holomorphic function of the twistor yields the electromagnetic field, a complex Yang–Mills triplet, and a two-component spinor, the first two as its second derivatives and the third as the potential's own surviving components. The three are not unified in the sense of a group that contains them, and the algebra does not identify their couplings; what is unified is their **origin**. Since the source's construction is an external programme, the corpus records this as the programme's structure and not as a result of the framework.

### The Triplet

The trace-free part of the same connection is a complex triplet whose strength the source writes in closed form through the electromagnetic one and the ratio $G$,

$$
F=\{-GF,\;iGF,\;-F\},
$$

with the repeated $F$ on the left the triplet and on the right the electromagnetic two-form. Its modulus in the complexified isotopic space equals the modulus of the electromagnetic field, and this is not an approximation: the three squares sum to

$$
(-GF)^2+(iGF)^2+(-F)^2=F^2\bigl(G^2-G^2+1\bigr)=F^2 ,
$$

which is an identity in $G$ and $F$ and was checked to $1.7\times10^{-15}$ on a hundred random complex pairs. The corpus records the modulus relation in the form it takes in the 1995 presentation, $\sum_a(L_{\mu\nu a})^2\propto(F_{\mu\nu})^2$, with a constant that the 1995 normalisation leaves open; written as components, the constant is fixed, and with these components it is one.

**The cancellation is the interesting part.** The identity holds because the first two components of the multiplier $\{-G,iG,-1\}$ have squares $G^2$ and $-G^2$. Had the second component been $G$ rather than $iG$, the modulus would have been $F^2(G^2+1)$ and the abelian field would not have been the length of the non-abelian one. So the modulus relation is a statement about the **complex structure** and not about the algebra of the triplet index: the two components that cancel do so because one carries the central $i$ and the other does not, and the three-dimensional index is being used as a complex three-space rather than as a real one. This is the same point the source makes when it observes that the Yang–Mills field of the construction is necessarily complex — its real and imaginary parts separately do not obey free equations, because the equations are nonlinear.

**And the internal direction is not free.** The multiplier $\{-G,iG,-1\}$ is built from $G$, which is the projective coordinate of the congruence. So the direction in which the non-abelian field differs from the abelian one is a function of the congruence's own direction, and the triplet carries no internal parameter that the congruence does not already carry. The multiplier is not null — its squared modulus is one — so the reading is not that the internal direction *is* the null direction; the reading is that the two are not independent, one being the image of the other. That is a strong claim and an unusual one, and the corpus records it without endorsing it: it says that in this construction an internal index and a spacetime direction are distinguished by where they sit in the formula rather than by their origin.

## The Caustic Is the Particle

For the effective curvature and for the electromagnetic field the singular locus is the same locus, and the twistor picture names it: the set of points whose line is tangent to the twistor surface. The coincidence is the source's, is recorded in *The Algebrodynamical Programme*, and is carried here **with the qualification that belongs to it: the associated Yang–Mills fields carry generically additional string-like singularities, so the coincidence is exact for the curvature and the electromagnetic field and is not claimed for the non-abelian ones.** Naming the locus a tangency turns the coincidence into a theorem of intersection theory: a point is singular for the field exactly when the algebraic resolution of $\Pi$ for $G$ degenerates, and a resolution degenerates exactly when the line and the surface are tangent, and the field is a function of the resolved $G$ and its derivatives. For the two abelian objects nothing else can happen, so their coincidence is forced.

**The static family is the test case, and it works exactly.** For the generator of the ring solution,

$$
\Pi=wG^2+2(z+ia)G-p ,
$$

the tangency condition $P=0$ gives $G=-(z+ia)/w$, and substituting it back into $\Pi=0$ leaves

$$
\Pi\big|_{P=0}=-\frac{x^2+y^2+(z+ia)^2}{w}=-\frac{r_*^2}{w},
$$

checked symbolically with $w=x-iy$ and $p=x+iy$. The tangency locus is therefore $r_*^2=0$ — the ring of radius $a$ in the plane $z=0$, with its two real conditions $x^2+y^2+z^2=a^2$ and $2az=0$. **The particle of the programme is the set of lines tangent to the twistor surface, and for the Kerr generator that set is the Kerr ring**, which is as direct a confirmation of the geometric reading as the construction admits.

**What the picture does and does not settle.** It settles why the singularities coincide, and it gives their dimension count. Tangency is one complex condition, hence two real conditions, so the singular set has codimension two: a surface generically in four coordinates, a curve when one coordinate is ignorable and the two conditions fall on three, and a point at a further degeneracy. That is the source's catalogue of points, strings and surfaces, and it is a count rather than an observation. What the picture does not settle is what the singularities *are* physically. The corpus records the programme's particle reading — a common singularity of the fields, with quantised charge — in the article that owns it, and does not adopt it here.

## What the Construction Is and Is Not

**It is not the Penrose transform.** The incidence geometry is the classical one, and the null quadric is the same quadric; but the object attached to a twistor here is the **general solution of a nonlinear first-order system**, not a solution of a linear massless field equation. There is no cohomology, no $\bar\partial$-closed form, no contour integral, and no transform in the sense of the twistor programme: the field is an algebraic function of the same $\Pi$ that defines the congruence, and the "transform" is differentiation. *Twistor Theory and Biquaternions* records the three senses in which the corpus's literature uses the word; this article is the sense it calls the congruence twistor, taken past the incidence relation to the fields.

**It bears on two of the open questions the introduction lists.** Question 1 asks whether the algebra's structure produces consequences or only reformulates known physics, to be judged by the richness of what it yields; question 4 asks for a relativistic theory of spinor fields whose classical precursor is the biquaternion Dirac equation. The construction here does something that neither of those programmes does: it yields a chiral two-component spinor, a Maxwell field and a non-abelian triplet from one holomorphic function, with no gauge principle imposed and no Dirac equation written down. It does so, however, on an algebra of coordinates rather than on the corpus's algebra of fields, so the answer is given in a neighbouring setting and does not transfer without a translation the corpus does not possess. Whether the construction is a derivation of the linear equations or only a very economical bookkeeping is the question it leaves open, and it is the right question to leave open.

**What it does not give.** No action, hence no canonical quantisation of the kind the corpus's quantisation articles presuppose. No superposition: a sum of two solutions satisfies the linear equations but not the congruence equation, which the programme article records as a selection rule and a cost. No dynamics beyond the algebraic constraint: the "time evolution" of a singular locus is the motion of a tangency, and it is determined, not postulated, which is either the construction's strength or its limitation depending on what one wanted. And no numerical prediction except the one the programme derives elsewhere.

## Summary

A congruence of null rays is a two-surface $S$ in projective twistor space; a spacetime point is a line $L_x$ in that space; the congruence's principal spinor at the point is the intersection $L_x\cap S$, and the number of its branches is the degree of the surface, by Bézout. The whole construction is that one correspondence, and the algebra that makes it computable is one pair of first-order relations, $\partial\lambda/\partial w=G\,\partial\lambda/\partial\upsilon$ and $\partial\lambda/\partial v=G\,\partial\lambda/\partial p$, satisfied by every function of the twistor because it is satisfied by the twistor's own components. Multiplying the pair gives the complex eikonal; cross-differentiating it gives a wave equation for the functions of $G$ and not for the general twistor function, with the obstruction computed; and written on the spinor $\xi=(1,G)$ the pair is the constraint that the programme imposes on its rescaling parameter. The condition for a rescaling to be a symmetry and the condition for a function to solve the eikonal are therefore one condition, whose solutions are the functions of the twistor.

From that pair everything else follows. The four-component twistor field has rank two — verified as an exact vanishing of every three-by-three minor at the rounding floor of forty-digit arithmetic, with the non-vanishing minors at $O(0.1)$, over three generating functions and a hundred points each — which is why it is a surface and why the rescaling group is a group. The group's orbits are the projective twistors, so the projective structure is derived from the restricted gauge symmetry rather than assumed, and the potential shifts by a gradient while the field strength stays fixed. Then three fields come out of one function: the electromagnetic field as the second derivatives of $\ln G$, guaranteed to obey the free Maxwell equations by the harmonicity that the pair supplies for a function of $G$; a complex Yang–Mills triplet whose modulus equals the electromagnetic field because the squares of its first two components cancel between $G^2$ and $(iG)^2$; and — the part not previously in the corpus — a two-component spinor inside the four-potential: the gauge $\xi_{0'}=1$ annihilates the first row of the potential array $\Phi_{B'A}$ by the source's (13), and the surviving pair $\varphi_0=\partial\ln G/\partial w=\partial G/\partial\upsilon$, $\varphi_1=\partial\ln G/\partial v=\partial G/\partial p$ satisfies the Weyl relations. Those relations carry the wave equation $\Box G=0$ beside an identity of mixed partials, so the reduction is recorded as a representation of the harmonicity and not as a new equation.

The singular locus is the tangency locus: a point is singular for the field exactly when the line and the surface are tangent, because the field is a function of the resolved $G$ and a resolution degenerates exactly there. For the static ring generator the condition reduces exactly to $r_*^2=0$, so the ring of the programme is literally the set of lines tangent to its twistor surface. What this settles is the coincidence of the two abelian singular loci and the dimension count of the tangency set; what it does not settle is what the singularities are, and the corpus leaves the programme's particle reading with the programme.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Z$, $Z_{AB}$ | Complex coordinate matrix of complexified Minkowski space |
| $\upsilon,v,w,p$ | The entries $Z_{00},Z_{11},Z_{01},Z_{10}$; $w=x-iy$, $p=x+iy$ on the real slice |
| $\xi=(\xi_0,\xi_1)$, $\tau=Z\xi$ | Principal spinor and the incident twistor |
| $\tau^{*}\xi-\xi^{*}\tau=0$ | Null-twistor condition; automatic for Hermitian $Z$ |
| $G=\xi_1/\xi_0$ | Principal ratio, the congruence's projective coordinate; gauge $\xi_0=1$ |
| $\kappa_0=wG+\upsilon$, $\kappa_1=vG+p$ | The two twistor components attached to $G$ |
| $T=(\xi,\tau)=(G,\kappa_0,\kappa_1)$ | The twistor of the point, written as one symbol where the group acts on it |
| $\Pi(G,\kappa_0,\kappa_1)$ | Generating (world) function; $S=\{\Pi=0\}$ is the twistor surface |
| $P=\partial\Pi/\partial G$ | Tangency condition: $P=0$ with $\Pi=0$ |
| $\partial\lambda/\partial w=G\,\partial\lambda/\partial\upsilon$, $\partial\lambda/\partial v=G\,\partial\lambda/\partial p$ | The pair of relations, obeyed by every twistor function $\lambda$ |
| $\Box=4\left(\partial^2/\partial\upsilon\,\partial v-\partial^2/\partial w\,\partial p\right)$ | The d'Alembertian in these coordinates |
| $\alpha(T)$ | Rescaling parameter; a symmetry exactly when it is a twistor function |
| $A\mapsto A+d\ln\alpha$ | Shift of the potential; $F=dA$ invariant |
| $\Lambda=\ln G$ | Field-generating function of the programme's presentation |
| $F_{00},F_{01},F_{11}$; $E_+,E_3,E_-$ | Independent components of the antiself-dual field, as second derivatives of $\Lambda$ in the programme's presentation and of $G$ in the 2016 paper's |
| $\varphi_0,\varphi_1$ | The two surviving components of the potential, $\varphi_0=\partial\ln G/\partial w$ and $\varphi_1=\partial\ln G/\partial v$ in the gauge $\xi_{0'}=1$ |
| $\{-GF,iGF,-F\}$ | Yang–Mills triplet; its modulus is $F$ |
| $r_*^2=x^2+y^2+(z+ia)^2$ | Ring condition; the tangency locus of the static generator is $r_*^2=0$ |

## Further Reading

- [Null Electromagnetic Fields and the Shear-Free Congruence](null-electromagnetic-fields-and-the-shear-free-congruence.html), for the null field, Bateman's representation, the principal null direction and the Mariot–Robinson theorem, which is the classical statement that a null field and a shear-free congruence determine one another.
- [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html), which owns the programme this article takes its twistor from: the generating system, the weak self-duality, the Yang–Mills triplet, the field from the derivatives of $\Pi$ alone, the charge quantisation and the particle reading.
- [Twistor Theory and Biquaternions](twistor-theory-and-biquaternions.html), for the incidence relation, the two spaces $S\oplus\bar S$, the Klein quadric, and the three senses in which the corpus uses the word twistor.
- [The Two-Sided Derivative over the Biquaternion Algebra](../articles_maths/the-two-sided-derivative-over-the-biquaternion-algebra.html), which owns the coordinate chart $\upsilon,v,w,p$, the determinant identity behind the complex eikonal, and the proof that the twistor-generated class is both null and harmonic.
- [The Spinor-Helicity Formalism and Biquaternions](the-spinor-helicity-formalism-and-biquaternions.html), for the massless momentum as a zero divisor, the rank-one factorisation of a null object, and the little group — the structures that the incidence relation's two-column decomposition is the geometric counterpart of.
- [The Yang–Mills Equation in Biquaternionic Form](the-yang-mills-equation-in-biquaternionic-form.html), for the differential Yang–Mills equation and its Bianchi identity, against which the algebraic triplet of this article should be read.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the two halves of a complexified two-form and the naming of the two signs, which this article's $F_{01}$ and its partners presuppose.
- V. V. Kassandrov and J. A. Rizcallah, "Maxwell, Yang–Mills, Weyl and eikonal fields defined by any null shear-free congruence", arXiv:1612.06718 [gr-qc] (2016), the paper this article was written around: the twistor form of the shear-free equations, the weakened gauge group and its projective orbits, the four-eikonal equation for the spinor components, the field through the derivatives of $\Pi$ alone, the Weyl spinor inside the potential, and the closed-form Yang–Mills triplet with its modulus. The paper is cited nowhere else in the corpus; the field algebra it belongs to is recorded under the programme article above.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1 and Vol. 2 (Cambridge University Press, 1984 and 1986), for the two-spinor calculus, the incidence relation, and the Kerr theorem in its standard form.
- G. C. Debney, R. P. Kerr and A. B. Schild, "Solutions of the Einstein and Einstein–Maxwell Equations", *Journal of Mathematical Physics* **10** (1969) 1842–1854, for the electrovacuum Kerr–Schild family that the linear generating functions produce.
- R. P. Kerr and W. B. Wilson, "Singularities in the Kerr–Schild metrics", *General Relativity and Gravitation* **10** (1979) 273, for the theorem that the static solutions of the congruence equation with a bounded singular set are exhausted by the Kerr solution.
