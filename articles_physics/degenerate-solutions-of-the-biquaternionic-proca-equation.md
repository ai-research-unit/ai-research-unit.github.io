# __Degenerate Solutions of the Biquaternionic Proca Equation__

## Introduction

*The Proca Equation in Biquaternionic Polar Variables* writes the potential $\tilde A_\Phi$ in the polar word of the material sector. That word is defined on the potentials whose quaternionic norm does not vanish, so its domain is the open set $\langle\tilde A_\Phi\rangle_\natural\neq0$, and its boundary is the set $\langle\tilde A_\Phi\rangle_\natural=0$, which is the light cone. This article takes the boundary as its subject.

The general theory of the boundary belongs to *Degenerate Solutions of the Biquaternionic Dirac Equation*. The cone, its two non-zero sectors $\Sigma_{01}$ and $\Sigma_{00}$, the failure of the polar word at $N=0$, and the fact that a non-zero element annihilated by a non-zero element is a zero divisor are established there for the full algebra, and none of them is re-derived here. What is new is the restriction of that theory to the Proca field. The restriction is not a smaller copy of the general case: the material sector is four real dimensional, its cone is the light cone, the field strength sits in a different carrier with a different cone, and the field is real, so its norm is one real equation where the algebra's norm is two.

Four results organise the answer, and each corrects a guess that comes naturally.

The first is that the failure set is a **hypersurface**. The material sector has four real dimensions and its cone is one real equation on them, so the degenerate set has dimension three and codimension one. On the full algebra the same cone is two real equations on eight, of dimension six and codimension two. A codimension-two failure leaves room for one chart with a small singular set; a codimension-one failure forces a piecewise chart with a genuine boundary, and that is exactly the shape of the material sector's word.

The second is that **only one sector appears**. Every non-zero lightlike potential satisfies $\tilde A_\Phi^2=\lambda\tilde A_\Phi$ with $\lambda=2ia'_t$, so it is in $\Sigma_{01}$ with a purely imaginary weight. The nilpotent sector $\Sigma_{00}$ meets the material sector at the apex and nowhere else.

The third is that **the field strength sits in the other sector**. The field strength is a pure vector, so it has zero trace, and a pure vector's square is a scalar; the cone of its carrier is therefore entirely $\Sigma_{00}$, and $\Sigma_{01}$ does not meet that carrier at all. The two objects of the Proca field carry one sector each. The trace decides, and the trace is the one number the two carriers cannot share.

The fourth is that **the plane-wave amplitude is strictly spacelike**. For a plane wave the norm of the amplitude is a transverse part plus a longitudinal part weighted by $k_m^2c^2/\omega^2$, a sum of two non-negative terms. It vanishes only when the transverse part vanishes and the longitudinal part is absent or the mass is zero. So no massive plane wave has a lightlike amplitude: a real massive wave is degenerate exactly at its nodes, and at zero mass the longitudinal mode is lightlike everywhere, where its field strength vanishes. Degenerate values are therefore a nodal or a superposition phenomenon, and not a property of a single amplitude.

**A note on the sector names.** The subscripts of $\Sigma_{01}$ and $\Sigma_{00}$ are the corpus's two predicates, $N=0$ and $B^2\neq0$, and not a count of anything. The Dirac article fixes the notation, and this article uses it unchanged.

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with $e_t=1$, $\vec e_\mu^2=-e_t$ and central scalar imaginary $i$; the material sector is $\mathbb{B}_\Phi=\mathrm{span}_\mathbb{R}\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$ and the vector part is $\mathbb{B}_V=\mathrm{span}_\mathbb{C}\{\vec e_x,\vec e_y,\vec e_z\}$; the quaternionic norm is $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$, real on $\mathbb{B}_\Phi$; the gradient is $\tilde\nabla_\Phi$ with conjugate $(\tilde\nabla_\Phi)^{\natural}$ and $\Box_\Phi=\Delta_\Phi-\partial^2/\partial{r'_t}^2$; and $k_m=mc/\hbar$.

## The Equation and the Field

**The equation.** The Proca equation is the single biquaternion equation

$$
\tilde\nabla_\Phi\tilde F=k_m^2\,\tilde A_\Phi,
\qquad
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
$$

with $\tilde A_\Phi\in\mathbb{B}_\Phi$ and $\tilde F\in\mathbb{B}_V$. The element form fixes it, together with the Lorenz condition $S=\mathrm{Sc}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)=0$, which the equation implies.

**Two carriers and not one.** The potential is one element of the material sector, which is four real dimensional. The field strength is one element of the vector part, which is six real dimensional. The two objects are not two readings of one element: they live in different subspaces, of different dimensions, over different fields.

**The norm on each carrier.** Write $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ with $a'_t$ and $\vec A$ real. The quaternion conjugation $\natural$ reflects the quaternion part and leaves the real coefficients alone, so

$$
\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^2+\vec A^2 ,
$$

which is real, and which is the Minkowski square of the four-vector $(a'_t,\vec A)$. Write $\tilde F=f_x\vec e_x+f_y\vec e_y+f_z\vec e_z$ with complex coefficients. Then

$$
\langle\tilde F\rangle_\natural=\sum_\mu f_\mu^2 ,
$$

which is complex in general, and which is $-F^2$ because a pure vector satisfies $\tilde F^{\natural}=-\tilde F$.

**Definition.** A field is **degenerate** at a point when its norm vanishes there; it is degenerate when the condition holds at every point of its domain. For the potential that is the light cone of field values; for the field strength it is $\tilde F^2=0$.

**A reading of the definition.** The norm that decides degeneracy is the quaternionic one, $\langle\cdot\rangle_\natural$. The definite form $\langle\cdot\rangle_*=\sum_\mu\lvert Q_\mu\rvert^2$ measures the size and never vanishes off the apex. A degenerate field has a size and no $\natural$ norm, and the two statements are not in conflict: they are two different forms, and only the indefinite one has a cone.

## The Lightlike Set of the Potential

**The intersection.** The degenerate potentials are the elements of

$$
\mathcal N\cap\mathbb{B}_\Phi=\Bigl\{\tilde A_\Phi=i\,a'_t\,e_t+\vec A:\ -(a'_t)^2+\vec A^2=0\Bigr\},
$$

the light cone of the four-vector $(a'_t,\vec A)$, apex included. It is one real equation on four real parameters.

**Why one equation and not two.** In the algebra the equation $\langle\tilde Q\rangle_\natural=0$ is complex, so it costs two real conditions and cuts the eight-dimensional algebra to six. On the material sector the same equation is real, because the coefficients are real and $\natural$ does not touch them. The carrier's reality halves the codimension, and the codimension is the algebraic statement of the causal character: a real four-vector is timelike, lightlike or spacelike, and the boundary between the first and the third is a hypersurface.

**The sector.** Squaring the potential gives

$$
\tilde A_\Phi^2=-\bigl((a'_t)^2+\vec A^2\bigr)+2i\,a'_t\,\vec A .
$$

On the light cone $(a'_t)^2=\vec A^2$, so the scalar part is $-2(a'_t)^2$ and the square is

$$
\tilde A_\Phi^2=-2(a'_t)^2+2i\,a'_t\,\vec A=2i\,a'_t\bigl(i\,a'_t\,e_t+\vec A\bigr)=\lambda\,\tilde A_\Phi,
\qquad
\lambda=2i\,a'_t .
$$

The weight is $\lambda=2Q_t$ with $Q_t=i\,a'_t$, which is the general formula of the Dirac article, and it is purely imaginary. It is non-zero: on the light cone $a'_t=0$ forces $\vec A^2=0$ and hence $\vec A=0$. So every non-zero lightlike potential is in $\Sigma_{01}$, with a weight that is the scalar potential up to the factor $2i$.

**There are no nilpotents.** The scalar part of the square is

$$
\mathrm{Sc}\bigl(\tilde A_\Phi^2\bigr)=-\bigl((a'_t)^2+\vec A^2\bigr),
$$

a negative real number unless the field vanishes. So $\tilde A_\Phi^2=0$ forces $\tilde A_\Phi=0$, and

$$
\Sigma_{00}\cap\mathbb{B}_\Phi=\{0\}.
$$

The restriction is worth stating plainly: the Proca potential never sits in the nilpotent sector, at any point of any solution. The nilpotent sector is not a rare case here; it is an absent one.

**The idempotent.** The sector's idempotent is $\tilde\Pi=\tilde A_\Phi/\lambda$. On the light cone put $\hat u=\vec A/a'_t$, which is a unit vector because $\lvert\vec A\rvert=\lvert a'_t\rvert$ and which carries the sign of $a'_t$. Then $\tilde A_\Phi=a'_t\,(ie_t+\hat u)$ and $\lambda=2i\,a'_t$, so

$$
\tilde\Pi=\frac{ie_t+\hat u}{2i}=\tfrac12\bigl(e_t-i\hat u\bigr),
$$

which is Hermitian, idempotent and null. The sector therefore keeps a null direction $\hat u$ and the weight $2i\,a'_t$; the direction is the spatial direction of the potential, and the weight is its scalar part. That is the material-sector form of the Dirac article's "a ray with a direction and a weight".

**What the boundary is not.** It is not a set of measure zero in the field's history. For a solution the local value of the potential moves in $\mathbb{B}_\Phi$, so the sign of the norm is a function of the point, and the boundary is a three-dimensional surface in spacetime whenever the field crosses it. The next sections say which solutions cross it, and the answer is less obvious than it looks.

## Two Carriers, Two Cones, Two Sectors

**The field strength's carrier.** The vector part has six real dimensions and its norm is complex, so its cone is two real equations on six and has dimension four. Its codimension is two, as in the full algebra, and for the same reason: the carrier is complex.

**The field strength's sector.** On the cone of $\mathbb{B}_V$ a field strength satisfies $\tilde F^2=0$; if it does not vanish it is therefore in $\Sigma_{00}$. It cannot be in $\Sigma_{01}$:

*Proposition.* $\Sigma_{01}\cap\mathbb{B}_V=\{0\}$.

*Proof.* Let $\tilde F$ be a pure vector and suppose $\tilde F^2=\lambda\tilde F$ with $\lambda\neq0$. A pure vector squares to a scalar, because the cross terms $\vec e_\mu\vec e_\nu+\vec e_\nu\vec e_\mu$ vanish for $\mu\neq\nu$; and $\lambda\tilde F$ is a pure vector. A scalar equal to a pure vector vanishes, so $\lambda\tilde F=0$, and since $\lambda\neq0$ the field vanishes.

**The trace decides.** The two results above are one result read twice. The sector is fixed by the trace: $\Sigma_{01}$ needs $\lambda=2Q_t\neq0$ and $\Sigma_{00}$ needs a vanishing trace. The material sector's trace is $2i\,a'_t$, which is non-zero for every non-zero lightlike potential; the vector part's trace is zero identically, because a pure vector has no scalar component. So each carrier can hold exactly one of the two sectors, and which one is decided before any field is chosen.

The table collects the comparison.

| | potential $\tilde A_\Phi$ | field strength $\tilde F$ |
| --- | --- | --- |
| carrier | $\mathbb{B}_\Phi$ | $\mathbb{B}_V$ |
| real dimension | $4$ | $6$ |
| norm | $-(a'_t)^2+\vec A^2$, real | $\sum_\mu f_\mu^2$, complex |
| cone, in equations | one real | two real |
| cone, dimension and codimension | $3$, and $1$ | $4$, and $2$ |
| trace $2Q_t$ | $2i\,a'_t$ | $0$ |
| $B^2$ | $\vec A^2$ | $\sum_\mu f_\mu^2$ |
| sector of the cone | $\Sigma_{01}$ | $\Sigma_{00}$ |

**One sector per object.** In the Dirac case one object, the field, contains both sectors: the kernel of a null multiplier carries one line of each. In the Proca case the two sectors are separated between the two objects, and no single element of the Proca field contains both. That is the sharpest structural difference from the Dirac article, and it is a consequence of the trace and of nothing else.

**A corollary on what the objects can be.** The potential is never a nilpotent; the field strength is never a scaled projection. Neither statement is an assumption about solutions. Both hold for every element of the respective carrier.

## Massive Plane Waves

**The mode.** Take

$$
\tilde A_\Phi=\tilde A_0\exp\bigl(-i\theta_{\mathrm{pwp}}\bigr),
\qquad
\theta_{\mathrm{pwp}}=\frac{\omega}{c}r'_t-\vec k_\Phi\cdot\vec r,
\qquad
\tilde P_\Phi=i\frac{\omega}{c}e_t+\vec k_\Phi ,
$$

with $\tilde A_0=i\,a'_t\,e_t+\vec a$ and $a'_t$, $\vec a$ real. The gradient acts as left multiplication by $i\tilde P_\Phi$ and its conjugate by $i\tilde P_\Phi^{\natural}$, so $\tilde F=\tilde F_0\exp(-i\theta_{\mathrm{pwp}})$ with $\tilde F_0=\mathrm{Vect}(i\tilde P_\Phi^{\natural}\tilde A_0)$.

**The two conditions.** The Klein–Gordon reduction gives the dispersion relation

$$
\frac{\omega^2}{c^2}-\vec k_\Phi^2=k_m^2 ,
$$

and the Lorenz condition fixes the time component of the amplitude,

$$
a'_t=\frac{c}{\omega}\,\vec k_\Phi\cdot\vec a .
$$

The amplitude data are the three real components of $\vec a$; $a'_t$ is not independent. With the momentum on the mass shell, which costs three parameters, a general massive plane wave has six.

**The norm of the amplitude.** Split $\vec a=\vec a_\parallel+\vec a_\perp$ along and across $\vec k_\Phi$. Substituting the Lorenz relation,

$$
\langle\tilde A_0\rangle_\natural=\vec a^2-\frac{c^2}{\omega^2}\bigl(\vec k_\Phi\cdot\vec a\bigr)^2
=\vec a_\perp^2+\vec a_\parallel^2\,\frac{k_m^2c^2}{\omega^2} .
$$

The display is exact, and it is a sum of two non-negative terms. Both vanish only if $\vec a_\perp=0$ and $\vec a_\parallel=0$, unless the second coefficient vanishes.

**The amplitude is never lightlike.** For $k_m\neq0$ the coefficient $k_m^2c^2/\omega^2$ is positive, so the norm vanishes only for the zero amplitude, and every non-zero amplitude of a massive plane wave is spacelike. The natural guess is the opposite one, that degeneracy is a codimension-one condition on the three amplitude parameters and is therefore met on a surface of them. The condition is indeed one equation, but the mass shell and the Lorenz condition together place the amplitude strictly inside the spacelike half, where the equation has no solution.

**The consequence at zero mass.** For $k_m=0$ the coefficient vanishes and $\langle\tilde A_0\rangle_\natural=\vec a_\perp^2$. The norm vanishes exactly for the longitudinal amplitude, $\vec a\parallel\vec k_\Phi$, and for no other. That amplitude is the pure-gauge direction, and the next section records that its field strength is zero.

**Two objects called a plane wave.** The element form writes $\tilde A_\Phi=\tilde A_0\exp(-i\theta_{\mathrm{pwp}})$, whose norm is $\langle\tilde A_0\rangle_\natural\exp(-2i\theta_{\mathrm{pwp}})$: a complex mode is degenerate everywhere or nowhere, and the amplitude decides. The polar form writes the real wave $\tilde A_\Phi=\tilde A_0\cos\theta_{\mathrm{pwp}}$, whose norm is

$$
\langle\tilde A_\Phi\rangle_\natural=\cos^2\theta_{\mathrm{pwp}}\,\langle\tilde A_0\rangle_\natural ,
$$

and which is degenerate at its nodes. The chart is a chart of $\mathbb{B}_\Phi$, that is, of real values, so the real wave is the object the chart sees.

**What a real massive wave degenerates to.** Its values are $\cos\theta_{\mathrm{pwp}}\tilde A_0$, spacelike wherever the cosine does not vanish and the apex where it does. So the degenerate set of a real massive plane wave is its nodal set, a family of parallel planes in spacetime, and no point of it carries a non-zero lightlike value. The polar chart's scale vanishes there and its direction survives, which is the polar article's statement that $\varepsilon$ flips at every node.

**The count.** A general plane wave has six parameters: three of momentum on the mass shell and three of amplitude after the Lorenz condition. The lightlike amplitudes form the empty subfamily at $k_m\neq0$, and at $k_m=0$ the longitudinal subfamily, three parameters of momentum and one of amplitude. That is not the count of degenerate solutions, because a real wave is degenerate at its nodes whatever its amplitude: the numbers count the degenerate amplitudes, and those are the empty family or the longitudinal one.

**The comparison with the Dirac case.** For a massive Dirac plane wave the phase is a unit of the algebra, so the norm of the field is the norm of the polarization times a unit that never vanishes: degeneracy is a property of the polarization, of codimension two in the free eight, and the degenerate family has nine parameters against eleven. For the Proca wave the chart sees a real scale and not a unit, so degeneracy is transported as a scale and appears at the nodes. The Dirac degeneracy is a property of the polarization, and the Proca degeneracy is a property of the point.

**Where degenerate values occur.** A superposition's local value is a sum of values, and a sum is not confined to one line of the carrier. Two lightlike values of different directions add to a value that is not lightlike:

$$
N\bigl((ie_t+\vec e_z)+(ie_t+\vec e_x)\bigr)=N\bigl(2ie_t+\vec e_x+\vec e_z\bigr)=-4+2=-2 ,
$$

which is timelike. So a superposition of modes passes through the cone, and its degenerate set is a family of surfaces in spacetime. A static solution reaches the apex at its nodes: the potential $i\,a'_t(\vec r)e_t$ with $(\Delta_\Phi-k_m^2)a'_t=0$ satisfies the Lorenz condition identically and the Klein–Gordon equation, hence the Proca equation, and it is degenerate on the surface where $a'_t$ vanishes.

**The branch a plane wave uses.** A real plane wave's amplitude is spacelike, so its values are spacelike off the nodes: the chart uses the spacelike branch, and the timelike branch is left to other solutions. A cosine wave with a timelike amplitude satisfies the scale equation and not the Lorenz condition, whose value on that wave is $\sin\theta_{\mathrm{pwp}}(\vec k_\Phi\cdot\vec a-\frac{\omega}{c}a'_t)$; no timelike amplitude makes that vanish, because $\lvert\vec k_\Phi\cdot\vec a\rvert$ is bounded by $\frac{\omega}{c}\lvert\vec a\rvert$ and that is less than $\frac{\omega}{c}\lvert a'_t\rvert$.

## The Lightlike Field Strength at Zero Mass

**The field strength's square.** A direct computation gives the amplitude's field strength in components,

$$
\tilde F_0=a'_t\,\vec k_\Phi-\frac{\omega}{c}\,\vec a-i\,\vec k_\Phi\times\vec a ,
$$

whose real part is $-\vec W$ with $\vec W=(\omega/c)\vec a-a'_t\vec k_\Phi$, and whose imaginary part is $\vec V=-\vec k_\Phi\times\vec a$; the scalar part, which the Lorenz relation makes vanish, is removed by $\mathrm{Vect}$. The cross term of the square vanishes, because $\vec V\cdot\vec W=-a'_t(\vec k_\Phi\times\vec a)\cdot\vec k_\Phi=0$, so the square is real:

$$
\tilde F_0^2=\vec V^2-\vec W^2=\lvert\vec k_\Phi\rvert^2\vec a^2-\bigl(\vec k_\Phi\cdot\vec a\bigr)^2-\frac{\omega^2}{c^2}\vec a^2+2\frac{\omega}{c}a'_t\,\vec k_\Phi\cdot\vec a-a_t^{\prime2}\lvert\vec k_\Phi\rvert^2 .
$$

Two substitutions reduce it. The Lorenz relation replaces $a'_t$, and the dispersion relation replaces $\omega^2/c^2-\vec k_\Phi^2$ by $k_m^2$. The result is

$$
\boxed{\;\tilde F_0^2=-k_m^2\,\langle\tilde A_0\rangle_\natural\;}
$$

**The identity's content.** The field strength's square is minus the mass squared times the potential's norm, for every plane wave. So the two objects' degeneracies are not independent: they coincide except where the mass vanishes.

**At zero mass.** For $k_m=0$ the square vanishes for every amplitude, and the field strength is a null bivector. It is non-zero for a transverse mode, since $\vec V=-\vec k_\Phi\times\vec a$ and $\vec W=(\omega/c)\vec a$ do not both vanish, so it is in $\Sigma_{00}$; and its two real vectors are perpendicular and of equal length, $\vec V^2=\vec W^2$, which is the radiative field with both invariants zero. The massless transverse modes therefore put the field strength on the cone of its carrier, in the nilpotent sector, at every momentum and every amplitude.

**At zero mass, the potential.** The same limit puts the potential on its own cone only for the longitudinal amplitude, by the previous section. There the field strength vanishes: the direction $\vec k_\Phi\times\vec a$ whose imaginary part it carries is zero, and the remaining part $a'_t\vec k_\Phi-(\omega/c)\vec a$ is zero because $a'_t=(c/\omega)\lvert\vec k_\Phi\rvert\lvert\vec a\rvert$ and $\omega/c=\lvert\vec k_\Phi\rvert$ at $k_m=0$.

**The two cones are not reached together.** At zero mass every mode with a non-zero field strength has a spacelike potential, and every mode with a lightlike potential has no field strength. So the sector assignment of the two objects is realised in complementary regimes: the field strength's degeneracy is generic, the potential's is confined to the gauge direction. One sentence states the pair of facts: the potential is lightlike exactly where the field strength is absent.

**Why the mass is the switch.** At $k_m\neq0$ the identity gives $\tilde F_0^2=-k_m^2\langle\tilde A_0\rangle_\natural$, and the norm of the amplitude is strictly positive, so the field strength's square is strictly negative. A massive plane wave's field strength is never null, and its second invariant is the potential's norm with a sign. The mass is what moves the field strength off its cone, and it does so for every mode at once.

**A caveat on superpositions.** Neither statement survives a sum of modes with different momenta. The field strength of a sum is not the sum of the field strengths, and its square is not the sum of the squares; a superposition of two massless modes of different momenta is generally not a null field. The sector statements of this section are statements about single modes, and the Dirac article's massless case has the same limitation: its two-sided field is generically a unit.

## The Polar Word and Its Boundary

**The word.** The polar article's chart is piecewise,

$$
\tilde A_\Phi=\varepsilon\,i\,r\,\tilde U_{\Psi,\mathrm b}\ \ (\langle\tilde A_\Phi\rangle_\natural<0),
\qquad
\tilde A_\Phi=r\,\tilde U_{\Psi,\mathrm b}\,\hat u\ \ (\langle\tilde A_\Phi\rangle_\natural>0),
$$

with $r>0$, $\varepsilon=\pm1$, $\tilde U_{\Psi,\mathrm b}$ a boost, and $\hat u$ a real unit vector locked to the direction of $\vec A$. Four parameters on each branch, and no branch on the light cone. The word is not derived here; the polar article derives it, and this article cites it.

**What the codimension explains.** The two branches exist because the failure set is a hypersurface: a connected open set cut by a hypersurface has two sides, and the sign of the norm labels them. On the full algebra the failure set is codimension two, so the complement is connected, and one word suffices there. That is the structural reason the material sector's word is piecewise and the spinor's is not, and it is a fact about the codimension and not about the fields.

**The origin of the codimension.** The material sector's norm is real, so its zero set is one equation. The reason is the reality of the four-vector: $a'_t$ and $\vec A$ are real numbers, and $\natural$ does not conjugate them. A complex amplitude has no such property, and its norm's zero set is complex codimension one, that is real codimension two.

**Where the boundary sits for a solution.** For a solution, the branch is a spacetime region, and the boundary is the set where the local value is lightlike. By the previous sections, a single massive mode meets it only at its nodes, where the value is the apex and the chart's scale is zero; a single massless longitudinal mode is entirely on it; and a superposition crosses it on surfaces, where the value is lightlike and not zero. The polar article's statement that the chart fails on "a family of three-dimensional surfaces" is therefore the statement about superpositions, and the plane-wave cases are its two extremes.

**The scale at the boundary.** On the boundary $r=0$, so the scale of the chart vanishes and the direction $\hat u$ survives alone. The apex is the one point where the direction is undetermined as well. The chart therefore loses its scale before it loses its direction, which is the polar article's statement that $r=0$ is only the corner of the failure set.

## What Degeneracy Is Not

**It is not a zero field.** The lightlike potential $ie_t+\vec e_z$ has $\langle\cdot\rangle_\natural=0$ and definite norm $2$, so it has a size and no $\natural$ norm. The exception is the node of a real field, where the value is the apex: there the field is zero and degenerate at once, and the coincidence is a property of that point and not of the definition.

**It is not a failure of the equation.** The Proca equation holds at a degenerate point as it holds anywhere, the Lorenz condition holds, and the field strength is defined. What fails is the reading of the potential in the chart's coordinates.

**It is not imposed by the mass.** The mass enters the identity $\tilde F_0^2=-k_m^2\langle\tilde A_0\rangle_\natural$ as a coefficient, and it is the mass that keeps the plane-wave amplitude strictly spacelike. So the mass acts on degeneracy through the amplitude: it removes the lightlike amplitudes and leaves the nodal degeneracy untouched.

**It is not two conditions on the potential.** On the material sector the norm is one real equation, so the degenerate set of the carrier is a hypersurface and not a codimension-two set. A reader who carries over the algebra's count looks for two conditions and finds one; the count changes because the carrier's reality does.

**It is not a condition on a single component.** What vanishes is a quadratic form, $-(a'_t)^2+\vec A^2$. No component need vanish, and no component is singled out.

**It is not the same statement for the two objects.** The potential's degeneracy and the field strength's are different conditions on different carriers, in different sectors, with different codimensions. The one identity that links them is the plane-wave identity of the previous section, and it links them through the mass.

## Summary

The degenerate solutions of the biquaternionic Proca equation are the solutions whose potential has vanishing quaternionic norm at a point, and the set is the light cone of field values.

The cone of the material sector is one real equation on four real parameters, of dimension three and codimension one, because the carrier is real and its norm is real. That codimension is why the polar word is piecewise: a hypersurface cuts the carrier into the timelike and spacelike halves, and the two branches of the word are those halves.

Every non-zero lightlike potential satisfies $\tilde A_\Phi^2=\lambda\tilde A_\Phi$ with $\lambda=2i\,a'_t$, so it is in $\Sigma_{01}$ with a purely imaginary weight and the idempotent $\tfrac12(e_t-i\hat u)$. The scalar part of the square is $-((a'_t)^2+\vec A^2)$, so the nilpotent sector meets the material sector only at the apex: the Proca potential is never a nilpotent.

The field strength's carrier is the complex vector part, of six real dimensions and codimension two, and its cone is entirely $\Sigma_{00}$: a pure vector squares to a scalar, so $\Sigma_{01}$ does not meet that carrier. The trace decides both assignments — $2i\,a'_t$ for the potential, zero for the field strength — and the two objects of the Proca field therefore carry one sector each, where the Dirac field carries both in one object.

For a plane wave, $\langle\tilde A_0\rangle_\natural=\vec a_\perp^2+\vec a_\parallel^2k_m^2c^2/\omega^2$, so no massive amplitude is lightlike: a real massive wave is degenerate exactly at its nodes, and at zero mass the longitudinal mode is lightlike everywhere, where the field strength vanishes. For every plane wave $\tilde F_0^2=-k_m^2\langle\tilde A_0\rangle_\natural$: at zero mass the field strength of every transverse mode is a non-zero nilpotent, in $\Sigma_{00}$, and at non-zero mass it is never null. The two cones are reached in complementary regimes, and the mass is the switch.

Degenerate values of the potential therefore arise from superpositions, which cross the cone on surfaces, and from the nodes of real fields, where the value is the apex. For a single mode the boundary is met only at the nodes, or not left at all.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_V$ | Complex three-dimensional vector part |
| $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ | Four-potential, $a'_t$ and $\vec A$ real |
| $\tilde F=\mathrm{Vect}((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi)$ | Field strength, a pure vector |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm; real on $\mathbb{B}_\Phi$ |
| $\langle\tilde Q\rangle_*=\sum_\mu\lvert Q_\mu\rvert^2$ | Definite norm; the size, never zero off the apex |
| $\mathcal N$ | The cone $\langle\tilde Q\rangle_\natural=0$, the zero divisors |
| $\Sigma_{01}$, $\Sigma_{00}$ | The sectors $Q^2=\lambda Q$ with $\lambda\neq0$, and $Q^2=0$ |
| $\lambda=2Q_t$ | The non-zero eigenvalue of a $\Sigma_{01}$ element |
| $\tilde\Pi=\tilde A_\Phi/\lambda$ | The idempotent of a lightlike potential, $\tfrac12(e_t-i\hat u)$ |
| $B^2=Q_x^2+Q_y^2+Q_z^2$ | Square of the vector part; $N=Q_t^2+B^2$ |
| $\tilde P_\Phi=i(\omega/c)e_t+\vec k_\Phi$ | Four-wavevector biquaternion |
| $\theta_{\mathrm{pwp}}=\omega r'_t/c-\vec k_\Phi\cdot\vec r$ | Plane-wave angle |
| $\tilde A_0=i\,a'_t\,e_t+\vec a$ | Plane-wave amplitude of the potential |
| $\vec a_\parallel$, $\vec a_\perp$ | The amplitude along and across $\vec k_\Phi$ |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- *The Proca Equation in Biquaternionic Polar Variables*, for the piecewise word, the light cone as the failure set of the chart, and the two brackets. This article takes the word's boundary as its subject and adds nothing to the word.
- *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the equation, the implied Lorenz condition, the reduction to the Klein–Gordon equation, and the three polarizations.
- *Degenerate Solutions of the Biquaternionic Dirac Equation*, for the general classification of the cone, the two sectors $\Sigma_{01}$ and $\Sigma_{00}$, and the failure of the polar word at $N=0$. That article's case is the full algebra; this article's case is the material sector, and the differences are the reason it is written.
- *The Meaning of N Regularity and Degeneracy*, for the norm, the cone, its strata and the spectral predicates that the sector names abbreviate.
- *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector*, for the vector part as the carrier of the field strength, and for the null bivectors of the split.
- *The Third Polarization and the Self-Dual Split of the Massive Field Strength*, for the longitudinal mode, and for the reason the mass keeps the field strength off its cone.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition 2001), for the zero divisors of a Clifford algebra, the nilpotents, and the rank-one idempotents.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966; second edition Birkhäuser, 2015), for the null fields of the algebra and the geometric reading of a lightlike vector as a direction.
