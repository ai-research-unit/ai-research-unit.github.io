# __The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces__

## Introduction

The polar word is a product of four factors, and each factor acts on the algebra in a way that is fixed by its type. The scale dilates, the central phase multiplies, the boost acts by congruence, and the rotor acts by conjugation. The two subspaces

$$
\mathbb{M}_+=\{X\in\mathbb{B}:X^{*}=X\},
\qquad
\mathbb{M}_-=\{X\in\mathbb{B}:X^{*}=-X\},
$$

are the Hermitian and anti-Hermitian subspaces. They are the two eigenspaces of the Hermitian conjugation, and they are the two sectors of the corpus: $\mathbb{M}_+$ carries the four-velocity and the field strength, $\mathbb{M}_-$ carries the four-position and the four-momentum. The polar factors preserve the two sectors, and the article computes how.

The main point is a distinction of factors. The word contains the positive Hermitian **boost factor** $B$, but the factor that acts on a four-vector is the **frame rotor**

$$
\tilde U_L=B^{-1/2}=\exp\Bigl(i\frac{\eta}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\frac{\eta}{2}\,e_t+i\sinh\frac{\eta}{2}\,\vec u_{\mathrm b}.
$$

The boost factor is the square of the inverse frame rotor. The action by $B$ doubles the rapidity with the opposite sign and is not the Lorentz transformation; the action by $\tilde U_L$ is. The article uses $\tilde U_L$ throughout the action and reserves $B$ for the word.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and central $i$. The quaternion conjugation is $\natural$, the coefficientwise conjugation is $\bar{\cdot}$, and the Hermitian conjugation is ${}^{*}=\overline{\ \cdot\ }^{\natural}$. The norm is $\langle X\rangle_{\natural}=XX^{\natural}$. The polar word is

$$
\tilde Q=r\exp(i\alpha)B\tilde q,
\qquad
B=\exp(-i\eta\vec u_{\mathrm b}),
\qquad
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, $\eta\ge0$, and unit axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$. The symbols $r,\alpha,\eta,\theta$ are those of *The Polar Element Representation of Biquaternions*; $\eta$ is the frame rapidity, written $\psi$ there, and $B=\exp(-i\eta\vec u_{\mathrm b})$.

## The Action Rule

For a factor $A$ of the polar word, the action on the algebra is the **congruence**

$$
\Theta_A(X)=A\,X\,A^{*}.
$$

The rule is uniform. For the central phase $A=\exp(i\alpha)$ it is the identity, because $A$ is central and unitary, $A^{*}=A^{-1}$:

$$
\Theta_{\exp(i\alpha)}(X)=\exp(i\alpha)X\exp(-i\alpha)=X.
$$

For the rotor $A=\tilde q$, which is real and unitary,

$$
\Theta_{\tilde q}(X)=\tilde q\,X\,\tilde q^{*}=\tilde q\,X\,\tilde q^{-1},
$$

the conjugation by the rotor. For the frame rotor $A=\tilde U_L$, which is Hermitian and of unit norm,

$$
\Theta_{\tilde U_L}(X)=\tilde U_L\,X\,\tilde U_L^{*}=\tilde U_L\,X\,\tilde U_L.
$$

The last equality uses $\tilde U_L^{*}=\tilde U_L$; the inverse is $\tilde U_L^{-1}=\tilde U_L^{\natural}$, not $\tilde U_L$ unless $\eta=0$. The congruence by a Hermitian factor is a **two-sided multiplication by the same factor**, and it is the action that produces a Lorentz boost.

The scale is not unitary. It acts by

$$
\Theta_r(X)=r\,X\,r=r^{2}X,
$$

the dilation by the square of the scale. The factor $r$ in the word is the scale of the element; the action on the algebra multiplies by $r^{2}$ because the scale appears on both sides.

**The action of the word.** The word is a product, and the action is the composition in the order of the factors:

$$
\Theta_{\tilde Q}(X)
=\Theta_{r}\circ\Theta_{\exp(i\alpha)}\circ\Theta_{\tilde U_L}\circ\Theta_{\tilde q}(X)
=r^{2}\,\tilde U_L\,\tilde q\,X\,\tilde q^{-1}\,\tilde U_L.
$$

This is the action of the **physical** word $\tilde U_L\tilde q$, with $\tilde U_L=B^{-1/2}$, not of the algebraic word $B\tilde q$. The algebraic word acts by $r^{2}B\tilde q\,X\,\tilde q^{-1}B$; replacing $B$ by $\tilde U_L$ is the square-root normalization that turns the boost factor into the group element. The central phase drops out of the congruence, and the product of the two non-central factors is the congruence by $\tilde U_L\tilde q$. The action is therefore the congruence by the frame rotor and the rotor, dilated by $r^{2}$.

**The action on states.** A state (a spinor) is acted on by left multiplication, not by congruence:

$$
\psi\longmapsto \tilde Q\,\psi.
$$

The two actions are different. The congruence preserves the sector and the interval; the left multiplication mixes the components of the spinor and is the action of the group on its defining module. The polar word's factors act on a state by left multiplication in the same order, and the phase and the scale are not in the kernel of that action.

## The Action on the Anti-Hermitian Subspace

An element of $\mathbb{M}_-$ is a four-position or a four-momentum,

$$
X=i a\,e_t+\vec b,
\qquad a,b_k\in\mathbb{R},
\qquad X^{*}=-X.
$$

The interval is the norm

$$
\langle X\rangle_{\natural}=X X^{\natural}=-a^{2}+\lvert\vec b\rvert^{2}.
$$

Write $\vec b=b_{\parallel}\vec u_{\mathrm b}+\vec b_{\perp}$, with $\vec b_{\perp}\perp\vec u_{\mathrm b}$. The congruence by the frame rotor gives

$$
a'=a\cosh\eta-b_{\parallel}\sinh\eta,
\qquad
b_{\parallel}'=b_{\parallel}\cosh\eta-a\sinh\eta,
\qquad
\vec b_{\perp}'=\vec b_{\perp}.
$$

The perpendicular part is untouched. The boost mixes the time component and the parallel space component, and the transverse component is the spectator. The interval is preserved:

$$
-a'^{2}+b_{\parallel}'^{2}+\lvert\vec b_{\perp}\rvert^{2}=-a^{2}+b_{\parallel}^{2}+\lvert\vec b_{\perp}\rvert^{2}.
$$

The transformation is the standard Lorentz boost of rapidity $\eta$ about $\vec u_{\mathrm b}$. The sign of the boost is the sign of the axis: reversing $\vec u_{\mathrm b}$ reverses the sign of the rapidity, which is the inverse transformation.

**The null cone.** On the cone $a=\lvert\vec b\rvert$, the formula gives

$$
a'+b_{\parallel}'=(a+b_{\parallel})e^{-\eta},
\qquad
a'-b_{\parallel}'=(a-b_{\parallel})e^{\eta}.
$$

The cone is preserved, and one of the two light-cone coordinates is contracted while the other is dilated. The product is invariant. A null vector stays null; the boost moves it along the cone.

**The rest frame.** A timelike vector with $a>0$ has a frame in which $\vec b'=0$. The rapidity is fixed by

$$
\tanh\eta=\frac{\lvert\vec b\rvert}{a},
$$

and the frame rotor of the inverse transformation is the positive square root of the boost factor, taken with the axis $\vec b/\lvert\vec b\rvert$. The polar word of the four-position has $r=(a^{2}-\lvert\vec b\rvert^{2})^{1/2}$ and $\alpha=\pi/2$; the boost factor is $B=-(i/c)\tilde V$ for the four-velocity.

**The infinitesimal form.** Differentiating at $\eta=0$,

$$
\frac{da}{d\eta}=-b_{\parallel},
\qquad
\frac{db_{\parallel}}{d\eta}=-a,
\qquad
\frac{d\vec b_{\perp}}{d\eta}=0.
$$

The generator is the differential operator $-b_{\parallel}\partial_a-a\partial_{b_{\parallel}}$, the Lorentz boost generator in the $(t,x_{\parallel})$ plane. The finite formula is its exponential.

## The Action on the Hermitian Subspace

An element of $\mathbb{M}_+$ is a four-velocity or a field strength,

$$
X=a\,e_t+i\vec b,
\qquad X^{*}=X.
$$

The norm is

$$
\langle X\rangle_{\natural}=a^{2}-\lvert\vec b\rvert^{2}.
$$

The congruence by the frame rotor gives

$$
a'=a\cosh\eta+b_{\parallel}\sinh\eta,
\qquad
b_{\parallel}'=b_{\parallel}\cosh\eta+a\sinh\eta,
\qquad
\vec b_{\perp}'=\vec b_{\perp}.
$$

The signs are opposite to the anti-Hermitian case. The interval is preserved:

$$
a'^{2}-b_{\parallel}'^{2}-\lvert\vec b_{\perp}\rvert^{2}=a^{2}-b_{\parallel}^{2}-\lvert\vec b_{\perp}\rvert^{2}.
$$

The four-velocity of a particle is the Hermitian element $V=\gamma(e_t+i\vec v/c)$; the boost acts on it by the same formula, and the rapidity is the rapidity of the relative velocity between the two frames.

**The null cone.** On the Hermitian cone $a=\lvert\vec b\rvert$,

$$
a'+b_{\parallel}'=(a+b_{\parallel})e^{\eta},
\qquad
a'-b_{\parallel}'=(a-b_{\parallel})e^{-\eta}.
$$

The roles of the two light-cone coordinates are exchanged relative to $\mathbb{M}_-$. The cone is preserved in both sectors, but the contracting and the dilating coordinates are interchanged.

**The infinitesimal form.** At $\eta=0$,

$$
\frac{da}{d\eta}=b_{\parallel},
\qquad
\frac{db_{\parallel}}{d\eta}=a,
\qquad
\frac{d\vec b_{\perp}}{d\eta}=0.
$$

The generator is $b_{\parallel}\partial_a+a\partial_{b_{\parallel}}$, the same Lorentz generator with the opposite sign. The two sectors carry the two signs of the boost.

## The Rotor

The rotor is a unit real quaternion. Its congruence is a conjugation,

$$
\tilde q\,X\,\tilde q^{-1},
$$

and it preserves both sectors because it commutes with the Hermitian conjugation:

$$
(\tilde q X\tilde q^{-1})^{*}
=\tilde q X^{*}\tilde q^{-1}.
$$

On the vector part it acts as the rotation of $\mathbb{R}^3$ by the angle $\theta$ about $\vec u_{\mathrm r}$; on the scalar part it acts trivially. In the anti-Hermitian sector,

$$
\tilde q(i a+\vec b)\tilde q^{-1}=i a+R_{\tilde q}\vec b,
$$

and in the Hermitian sector,

$$
\tilde q(a e_t+i\vec b)\tilde q^{-1}=a e_t+iR_{\tilde q}\vec b.
$$

The rotation is the same in both sectors. The rotor does not mix the time component with the space components; it rotates the space components and leaves the time component alone.

**The quarter turn.** For $\theta=\pi/2$ about $\vec e_z$,

$$
\tilde q=\frac{1}{\sqrt2}(e_t+\vec e_z),
\qquad
\vec e_x\mapsto\vec e_y,
\qquad
\vec e_y\mapsto-\vec e_x,
\qquad
\vec e_z\mapsto\vec e_z.
$$

The map is the rotation of the $(x,y)$ plane. The example is the smallest nontrivial rotor, and it is the one used in the product example below.

## The Central Phase and the Scale

The central phase is in the kernel of the congruence:

$$
\exp(i\alpha)X\exp(-i\alpha)=X.
$$

It is not in the kernel of the left action on a state: $\psi\mapsto\exp(i\alpha)\psi$ multiplies the spinor by a phase. The distinction is the reason the phase is invisible on the four-vector and visible on the wavefunction.

The scale acts by $r^{2}$ on the algebra:

$$
r\,X\,r=r^{2}X.
$$

It preserves both sectors and multiplies the interval by $r^{4}$:

$$
\langle r^{2}X\rangle_{\natural}=r^{4}\langle X\rangle_{\natural}.
$$

The factor $r^{2}$, not $r$, is the dilation of the action. The word's scale is the square root of the dilation; the norm of the element is the square root of the determinant, and the action sees the determinant.

## The Product of the Factors

The action of the word is the composition of the actions. The central phase and the scale are central and may be moved; the frame rotor and the rotor do not commute, and their order is the order of the word.

**The rotor first, then the boost.** For the word $\tilde U_L\tilde q$ acting on $X$,

$$
X\longmapsto \tilde U_L\,\tilde q\,X\,\tilde q^{-1}\,\tilde U_L.
$$

The rotor rotates the vector part; the boost then acts on the rotated vector. The composition is not the boost of the original components unless the axis of the rotor is parallel to the boost axis.

**The boost first, then the rotor.** For the reversed word $\tilde q\tilde U_L$,

$$
X\longmapsto \tilde q\,\tilde U_L\,X\,\tilde U_L\,\tilde q^{-1}.
$$

The two results differ by the rotor

$$
\tilde q^{-1}\tilde U_L^{-1}\tilde q\tilde U_L,
$$

which is the Thomas–Wigner rotation of the pair. The rotation is the obstruction to the two actions commuting.

**The two orders in numbers.** Take the anti-Hermitian element $X=i e_t+0.6\vec e_x$, the rotor of a quarter turn about $\vec e_z$, and the boost of rapidity $\eta=0.693147181$ about $\vec e_x$.

- Rotor first: $X\mapsto i e_t+0.6\vec e_y$, then the boost along $\vec e_x$ leaves the perpendicular part and gives

$$
i\cosh\eta\,e_t-\sinh\eta\,\vec e_x+0.6\vec e_y
=1.25i\,e_t-0.75\vec e_x+0.6\vec e_y.
$$

- Boost first: $X\mapsto 0.8i\,e_t$, the rest frame, and then the rotor leaves it unchanged:

$$
0.8i\,e_t.
$$

The two results are not the same transformation of the same vector. The two products differ by the rotor

$$
\tilde q^{-1}\tilde U_L^{-1}\tilde q\tilde U_L,
$$

which is the product of the rotated boost and the inverse boost. It is a rotation only when the two axes are parallel; in general it contains the Thomas–Wigner rotation, which is the subject of *The Lorentz Group in Biquaternionic Form — Structure and Representations*. The reversed order conjugates the boost axis by the rotor before the boost is applied.

## The Boost Factor and the Frame Rotor

The word contains $B=U_L^{-2}$, and the action contains $U_L$. The difference is a factor of two in the exponent, and it is worth displaying.

The congruence by $B$ is the congruence by $U_L^{-2}$, which is the boost of rapidity $-2\eta$:

$$
B\,X\,B=U_L^{-2}\,X\,U_L^{-2}
=\Theta_{U_L^{-1}}\bigl(\Theta_{U_L^{-1}}(X)\bigr).
$$

For the four-position $X=i e_t+0.6\vec e_x$ and $B=1.25e_t-0.75i\vec e_x$, the action by $B$ gives

$$
B\,X\,B=3.25i\,e_t+3.15\vec e_x,
$$

which is not the rest frame and not the original vector. The action by the inverse frame rotor $B^{-1/2}=1.06066e_t+0.35355i\vec e_x$ gives the rest frame $0.8i e_t$. The correct action is the one by a square root of the inverse boost factor, with the sign of the axis chosen so that the boost points from the lab to the rest frame. A calculation that uses the boost factor of the polar word directly as the group element is off by a factor of two in the rapidity; a calculation that uses the scale of the word directly in the action is off by a square.

## The Sector Preservation

Every factor of the word preserves the two sectors, and the reason is the same in each case.

- **Scale.** $r$ is real and central; $rXr$ is Hermitian iff $X$ is.
- **Phase.** $\exp(i\alpha)$ is central; the congruence is the identity.
- **Boost.** $\tilde U_L$ is Hermitian, so $\tilde U_L X\tilde U_L$ is Hermitian iff $X$ is.
- **Rotor.** $\tilde q$ is real, so it commutes with the Hermitian conjugation.

The actions therefore split into two maps,

$$
\Theta_{\tilde Q}^{+}:\mathbb{M}_+\to\mathbb{M}_+,
\qquad
\Theta_{\tilde Q}^{-}:\mathbb{M}_-\to\mathbb{M}_-,
$$

and each is a linear map of the corresponding real vector space. The map on $\mathbb{M}_-$ is the four-vector representation; the map on $\mathbb{M}_+$ is the Hermitian representation. They are not independent: the same parameters $r,\alpha,\eta,\theta$ act on both, and the pair of maps is the content of the polar word.

## The Action on a State

A spinor is a two-component complex column, and the biquaternion acts on it by left multiplication:

$$
\psi\longmapsto \mathsf M_2(\tilde Q)\psi.
$$

The matrix of the polar word is the product of the matrices of the factors,

$$
\mathsf M_2(\tilde Q)
=r\exp(i\alpha)\mathsf M_2(B)\mathsf M_2(\tilde q).
$$

The scale multiplies the spinor, the phase multiplies it by a phase, the boost mixes its two components with hyperbolic coefficients, and the rotor mixes them with trigonometric coefficients. The left action does not preserve the norm of the spinor in the same way as the congruence; it preserves the Hermitian form up to the determinant, and the determinant is the norm of the biquaternion.

The distinction between the two actions is the distinction between a four-vector and a spinor. The four-vector is a bilinear object, $X=\psi\psi^{*}$, and the congruence is the induced action on the bilinear. The spinor is the linear object, and the left multiplication is its action. The polar word acts on both, and the two actions are the two columns of the representation theory.

## Summary

The polar factors act by congruence, not by conjugation by the inverse. The scale dilates by $r^{2}$; the phase is in the kernel; the frame rotor $\tilde U_L=B^{-1/2}$ acts by $\tilde U_L X\tilde U_L$ and produces the Lorentz boost of rapidity $\eta$; the rotor acts by $\tilde q X\tilde q^{-1}$ and produces the spatial rotation. The two sectors $\mathbb{M}_+$ and $\mathbb{M}_-$ are preserved, with the boost formulas

$$
\begin{aligned}
\mathbb{M}_-:\quad & a'=a\cosh\eta-b_{\parallel}\sinh\eta,\quad
b_{\parallel}'=b_{\parallel}\cosh\eta-a\sinh\eta,\\
\mathbb{M}_+:\quad & a'=a\cosh\eta+b_{\parallel}\sinh\eta,\quad
b_{\parallel}'=b_{\parallel}\cosh\eta+a\sinh\eta.
\end{aligned}
$$

The word's boost factor is the square of the inverse frame rotor; the action by the factor doubles the rapidity, and the action by its square root is the physical one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{M}_+$ | the Hermitian subspace, $X^{*}=X$ |
| $\mathbb{M}_-$ | the anti-Hermitian subspace, $X^{*}=-X$ |
| $X=i a+\vec b$ | an element of $\mathbb{M}_-$ |
| $X=a+i\vec b$ | an element of $\mathbb{M}_+$ |
| $a,b_{\parallel},\vec b_{\perp}$ | the time component, the parallel and transverse space parts |
| $\Theta_A(X)=AXA^{*}$ | the congruence by a unitary factor |
| $B=\exp(-i\eta\vec u_{\mathrm b})$ | the positive Hermitian boost factor |
| $\tilde U_L=B^{-1/2}$ | the frame rotor |
| $\tilde q$ | the rotor |
| $r,\alpha$ | the scale and the central phase |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_physics/the-polar-element-representation-of-biquaternions.md`), the word and the factors.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), the positive-unitary decomposition.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`), the real-quaternion grouping.
- *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), the axis-angle grouping.
- *The Polar Decomposition of Biquaternions in Practice* (`articles_physics/the-polar-decomposition-of-biquaternions-in-practice.md`), the algorithm and the output.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_physics/the-polar-element-representation-and-remarkable-subspaces.md`), the invariant subspaces.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), the group action.
