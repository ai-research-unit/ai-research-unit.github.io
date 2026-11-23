# __The Field Strength as $(1,0)\oplus(0,1)$__

## Introduction

A field strength is a two-form, and a two-form in four dimensions has six components — the same six as the Lorentz algebra. The Hodge dual is a complex structure on the six-dimensional space, and its $\pm i$ eigenspaces split the field into two halves of three complex components each. Those halves are the two three-dimensional complex representations of the Lorentz algebra, $(1,0)$ and $(0,1)$, the two commuting complex triples of *The Two Commuting Complex Triples*, and they are the two helicities of the radiation field. So the field strength of a six-component two-form carries exactly the labels $(1,0)\oplus(0,1)$: the same six that the algebra carries in its adjoint, split the same way.

This article is the field-theoretic reading of the block's structural articles. It states the field strength as a bivector and as an element of the Lie algebra, defines the dual and its square, performs the split, identifies the Riemann–Silberstein half, derives the transformation law and the statement that the halves transform by the tensor action and not by the congruence, and writes the Bianchi identity and the field equation as one complex equation.

The algebra and the sign conventions are those of the corpus's field-strength articles, and this article does not restate them. *The Field-Strength Biquaternion and Its Invariants* supplies the field-strength biquaternion, the Hodge dual and the invariants; *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Bivector Plane* supplies the projectors and the naming of the two signs; *Exercise: Duality Rotation and the Riemann–Silberstein Vector* supplies the duality rotation and the warning about the transformation law; *Maxwell's Equations in the Biquaternionic Formulation* supplies the potential and the gauge structure. The block adds only the group-theoretic reading.

## The Field Strength as a Bi-Vector

### The Two-Form

$$
F=\tfrac12\sum_{\imath,\jmath}F_{\imath\jmath}\,dR_{\imath}\wedge dR_{\jmath},
\qquad
F_{\imath\jmath}=\frac{\partial A_{\jmath}}{\partial R_{\imath}}-\frac{\partial A_{\imath}}{\partial R_{\jmath}},
$$

with the six independent components organised into the electric and magnetic three-vectors:

$$
F_{0k}=E_\imath,\qquad F_{k\chi}=-\epsilon_{k\chi\kappa}cB_\kappa .
$$

So the two-form's six real components are exactly the six real numbers an observer calls the electric and magnetic fields, and the split into $E$ and $B$ is a choice of observer's frame.

### The Carrier in the Algebra

The bivector space is the vector part of $\mathbb{B}$: the six-dimensional real space spanned by the products $\vec e_\imath\vec e_\chi$, equivalently the scalar-free part of the algebra, equivalently the Lorentz Lie algebra itself. The corpus's field-strength biquaternion

$$
\tilde F=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H
$$

is an element of that space, and its components are the components of $F$.

### The Lie-Algebra Reading

Since the bivector space *is* $\mathfrak{so}(1,3)$, the field strength is a Lie-algebra-valued field, and the identification is not an analogy. That single fact decides the transformation law below, and it is the reason the field strength's action is the adjoint and not the congruence.

### What the Six Components Are Not

They are not a four-vector and not a pair of three-vectors glued together by hand. A four-vector has four components and a pair of three-vectors has six, and the six of a two-form are the *antisymmetric* six: they transform into one another under boosts in a way that mixes electric and magnetic components. That mixing is the physical content of "a moving charge's electric field has a magnetic field", and it is what the two-form's transformation law expresses.

## The Hodge Dual

### The Definition

In four dimensions the Hodge dual of a two-form is a two-form:

$$
\star F_{\imath\jmath}=\tfrac12\sum_{\rho,\sigma}\varepsilon_\rho\varepsilon_\sigma\,\epsilon_{\imath\jmath\rho\sigma}F_{\rho\sigma},
$$

and on the $(\vec E,\vec B)$ pair it acts as

$$
\star:\ (\vec E,\vec B)\longmapsto\bigl(c\vec B,\,-\vec E/c\bigr).
$$

The action is a quarter turn in each of the three planes spanned by $(E_\imath,cB_\imath)$.

### Its Square

$$
\star^{2}=-1 .
$$

The dual is therefore a complex structure on the six-dimensional bivector space, and its eigenvalues are $\pm i$. The minus sign is the Lorentzian sign pattern's: in four Euclidean dimensions the dual's square is $+1$ and the split becomes $\pm1$ rather than $\pm i$.

### On the Algebra's Vector Part

In the algebra the dual is multiplication by a scalar imaginary:

$$
\star\tilde F=-i\,\tilde F ,
$$

which is the identity the corpus's split article proves. So the two halves are the two eigenspaces of the *left multiplication* by $i$ on the complexified vector part, and the split is an algebraic operation on the element rather than a tensor operation on the components.

### Why the Two Descriptions Agree

Multiplication by $i$ on the complexified vector part and the Hodge dual on the two-form are the same complex structure, because the bivector basis is real and the dual's action on it is the multiplication by $i$ up to the orientation convention. So the tensor and the algebraic readings of "self-dual" are the same reading.

## The Split

### The Two Eigenfields

$$
\mathcal{F}_{+}=\tfrac12\bigl(F+i\star F\bigr),\qquad
\mathcal{F}_{-}=\tfrac12\bigl(F-i\star F\bigr),
\qquad
\star\mathcal{F}_{\pm}=\mp i\,\mathcal{F}_{\pm},
$$

and $F=\mathcal{F}_{+}+\mathcal{F}_{-}$. The two are the **self-dual** and **anti-self-dual** halves.

### The Naming

The corpus fixes the naming in the sign convention of the display: the $\star$-eigenvalue $-i$ half is the self-dual one, and it is the half that the Riemann–Silberstein combination $\vec N=\vec E+ic\vec B$ represents:

$$
F+i\star F\ \longleftrightarrow\ 2\vec N .
$$

The opposite naming is used in some of the literature, and reversing the orientation density exchanges the names and changes nothing else. A reader must therefore check the convention before comparing two sources, and this article uses the corpus's.

### The Two Complex Triples

Each half is a three-dimensional **complex** space, and each carries one of the two three-dimensional complex representations of the Lorentz algebra — the two $\mathfrak{sl}_2$ summands of the complexification, written $(1,0)$ and $(0,1)$ in the labelling by a pair of half-integers:

$$
\mathcal{F}_{+}\in(1,0),\qquad \mathcal{F}_{-}\in(0,1).
$$

So the split of the field strength is the same split that *The Two Commuting Complex Triples* performs on the algebra, and the two halves are labelled by the two triples.

### The Reality Condition

For a **real** field $F$ the halves are complex conjugates:

$$
\overline{\mathcal{F}_{+}}=\mathcal{F}_{-},
$$

so the anti-self-dual half carries no data beyond the self-dual one, and $\vec N$ alone contains the six real components of $(\vec E,\vec B)$. On the complexified field space the two halves are independent, and only there does the pair of triples act independently.

That is the precise content of "the field strength is the sum of two self-dual halves": the sum is a sum of conjugate halves for a real field, and a sum of independent halves for a complexified one.

## The Riemann–Silberstein Vector

### The Definition of $\vec N$

$$
\vec N=\vec E+ic\vec B,
\qquad
\tilde F=i\sqrt{\epsilon}\,\vec N .
$$

The vector is complex, its real part is the electric field, and its imaginary part is the magnetic induction in units of $c$. So the six real components are packed into three complex ones.

### The Two Real Equations

In a region with no sources, Maxwell's equations are

$$
\vec\nabla_\Phi\cdot\vec E=0,\quad
\vec\nabla_\Phi\cdot\vec B=0,\quad
\vec\nabla_\Phi\times\vec E=-\partial_t\vec B,\quad
\vec\nabla_\Phi\times\vec B=\frac{1}{c^{2}}\partial_t\vec E .
$$

Substituting $\vec N$ collapses them pairwise:

$$
\vec\nabla_\Phi\cdot\vec N=0,
\qquad
\vec\nabla_\Phi\times\vec N=\frac{i}{c}\,\partial_t\vec N .
$$

The first combines Gauss's law with the absence of magnetic charge; the second combines Faraday's law with Ampère's law. Each is one complex equation, so the four real equations become two.

### The Verification

The collapse is checked on a plane wave. With $2\pi\vec\nu_{\Phi}=\omega\hat z/c$, a right-handed triad $\vec B=\hat k\times\vec E/c$ and the combination $\vec N=\vec E+ic\vec B$, the divergence vanishes identically, and the curl equation holds for one circular polarisation with the eigenvalue $2\pi\vec\nu_{\Phi}\times\vec N=-i\omega\vec N/c$, reproducing $\vec\nabla_\Phi\times\vec N=\frac ic\partial_t\vec N$ under $\partial_t\to-i\omega$ and $\vec\nabla_\Phi\to 2\pi i\vec\nu_{\Phi}$.

For the opposite circular polarisation the same convention gives $\vec N=0$: the mode is purely anti-self-dual in this naming, and the vanishing of $\vec N$ is the statement that the self-dual half of that mode is zero.

### The Helicity Reading

So the two circular polarisations are the two eigenfields: one is annihilated by the self-dual projector and the other is annihilated by the anti-self-dual one, and the two nonzero halves are the two helicities $\pm1$. That is why the split is called a helicity decomposition, and why the field's two degrees of freedom are the two halves and not the six components.

## The Transformation Law

### The Adjoint, Not the Congruence

The field strength is Lie-algebra-valued, so the Lorentz group acts on it by the **adjoint**:

$$
\tilde F\longmapsto\mathrm{Ad}_{\tilde U}(\tilde F)=\tilde U\tilde F\tilde U^{-1},
$$

and not by the congruence $\tilde U\tilde F\tilde U^{*}$ that acts on momenta and on four-vectors. That is the corpus's statement that the biquaternion proof of the split uses the antisymmetric-tensor action and not the four-vector rotor conjugation, and it is the reason the two actions of *The Two Actions of One Group: Adjoint and Congruence* must be kept apart here.

### Why the Congruence Fails

The congruence is an isometry of the norm and not an automorphism of the algebra, so it does not preserve the bivector space as a Lie algebra. Applied to a field strength it gives the right answer for rotations — where the two actions coincide — and the wrong answer for boosts. So a computation that uses the congruence on $\tilde F$ passes every rotation test and fails on every boost, which is the worst failure mode and the reason the warning is stated twice in the corpus.

### The Two Halves Under the Adjoint

The adjoint preserves the split, because it preserves the complex structure:

$$
\mathrm{Ad}_{\tilde U}(\star\tilde F)=\star\,\mathrm{Ad}_{\tilde U}(\tilde F),
$$

since both are built from the same invariant tensors. So each half is preserved, and on each half the adjoint acts through the corresponding $\mathfrak{sl}_2$ summand:

$$
\mathrm{Ad}_{\tilde U}\big|_{\mathcal{F}_{+}}=\text{the }(1,0)\text{ action},\qquad
\mathrm{Ad}_{\tilde U}\big|_{\mathcal{F}_{-}}=\text{the }(0,1)\text{ action}.
$$

### Where the Independence Ends

Over $\mathbb{C}$ the two actions are independent, and that is the sense in which the field strength is a sum of two independent halves. Over $\mathbb{R}$ they are tied by the reality condition, which is why a real field's two halves are not separately observable: only their combination $\vec E$ and $\vec B$ is, and the split is a change of basis in the field space and not a decomposition into two physical fields.

## The Potential and the Gauge Shift

### The Potential as a Vector

The field strength is not the fundamental object of the theory. It is the derivative of a **potential** $A$, a one-form: one coefficient multiplying the time direction, three multiplying the space directions. Under the Lorentz group a one-form transforms as a vector, so its carrier is $(\tfrac12,\tfrac12)$, the same carrier as the momentum and as the coordinate. The field strength, a two-form, has the carrier $(1,0)\oplus(0,1)$. The map between the two carriers is the exterior derivative:

$$
F=dA .
$$

### The Gauge Shift

The potential is not unique. For any function $\chi$ of the coordinates,

$$
A\ \longmapsto\ A+d\chi
$$

gives the same field strength, because

$$
d(A+d\chi)=dA+d^{2}\chi=dA ,
$$

and $d^{2}=0$ is the statement that mixed partial derivatives commute. So the shift is a symmetry of the theory and not of the potential, and the physical content is the equivalence class.

### The Potential as a Connection and the Field Strength as Its Curvature

A one-form $A$ assigns to each direction of a curve a rate: $A(\dot x)$ is the component of $A$ along the motion. That is what a connection does, and the field strength is its curvature, the antisymmetric part of the derivative of the connection:

$$
F_{\imath\jmath}=\partial_{\imath} A_{\jmath}-\partial_{\jmath} A_{\imath} .
$$

For an abelian connection the curvature is gauge invariant, which is the calculation of the previous subsection; for a non-abelian one the curvature would acquire a commutator $[A_{\imath},A_{\jmath}]$ and would transform in the adjoint. The abelian case is the one the block uses, and the absence of the commutator is the reason the field strength's carrier is the bivector and not a tensor product of two vector carriers.

### Why the Two Carriers Behave Differently Under the Shift

The shift adds a gradient, and a gradient is a one-form: the shift moves the potential **within its own carrier**, $(\tfrac12,\tfrac12)$ into $(\tfrac12,\tfrac12)$. That is why the $(1/2,1/2)$ carrier is not invariant under the shift as a *space of fields* — infinitely many potentials describe one field, and the shift is the redundancy.

The field strength's carrier $(1,0)\oplus(0,1)$ is untouched by the shift, because $d$ applied to the exact part gives zero. So the two statements are the two halves of one fact:

- the field strength is invariant under the shift, and its carrier therefore carries a representation of the group and nothing more;
- the potential is not, and its carrier carries a representation only after the exact one-forms are quotiented out.

The quotient is the reason the potential's longitudinal and scalar parts are not physical, and it is the representation-theoretic form of the statement that the photon has two helicities and not four.

## The Bianchi Identity and the Field Equation

### The Two Equations

With $F=dA$ the identity

$$
dF=0
$$

is automatic and is the Bianchi identity; it is equivalent to the two homogeneous Maxwell equations. The field equation in vacuum is

$$
d\star F=0,
$$

equivalent to the two inhomogeneous equations with zero sources. So the content of the free field theory is two equations for one object, and they are of the same differential order and the same form.

### The Single Complex Equation

Let $\mathcal{F}=F+i\star F$. Since $F$ is real,

$$
d\mathcal{F}=dF+i\,d\star F,
$$

so

$$
d\mathcal{F}=0\iff dF=0\ \text{and}\ d\star F=0 .
$$

The real part of the complex equation is the Bianchi identity and the imaginary part is the field equation. That is the article's title in one line: one complex equation for the self-dual half carries both the identity and the equation, because the two are the real and imaginary parts of a single statement.

### Why This Is Not a Trick

It is not a trick because $d\mathcal{F}=0$ is four complex equations on three complex components, and the four are not independent: $d^{2}=0$ gives one relation among them, so the system imposes exactly three complex conditions on three complex unknowns. That is $6$ real conditions on $6$ real components, which is the same count as the four real Maxwell equations of a free field.

The economy is the same economy as writing the two real equations of a plane wave as one complex equation: the complexification is a change of basis in which the two real conditions become one complex condition.

### With Sources

With sources the field equation becomes $d\star F=\star j$ and the complex equation acquires an inhomogeneous right-hand side,

$$
d\mathcal{F}=\star j ,
$$

with $j$ the current one-form. The Bianchi identity remains automatic, so the sourced theory is one complex inhomogeneous equation and one identity.

### The Reading

The physical interpretation is that the electric and magnetic fields are the real and imaginary parts of one complex field, that the two halves of that field are the two helicities, and that the pair of Maxwell equations is one equation in the complex basis. The split is therefore both a group-theoretic statement — the two triples — and an equation-level statement — one complex equation instead of two real ones.

## Summary

A field strength is a two-form, hence an element of the Lorentz Lie algebra, with six real components. The Hodge dual squares to $-1$, so it is a complex structure whose $\pm i$ eigenspaces split the complexified field into a self-dual and an anti-self-dual half of three complex components each, the two three-dimensional complex representations $(1,0)$ and $(0,1)$ — the two commuting complex triples. The self-dual half is the Riemann–Silberstein vector $\vec N=\vec E+ic\vec B$, in which the four vacuum Maxwell equations collapse into $\vec\nabla_\Phi\cdot\vec N=0$ and $\vec\nabla_\Phi\times\vec N=\frac ic\partial_t\vec N$, one complex equation for the two helicities. The field transforms by the adjoint and not by the congruence, so the halves are preserved by the Lorentz action and are conjugate for a real field; over $\mathbb{C}$ they are independent. The field is the curvature $F=dA$ of a potential one-form, whose carrier is $(\tfrac12,\tfrac12)$, and the gauge shift $A\mapsto A+d\chi$ leaves $F$ alone because $d^{2}=0$; so the potential's carrier is quotiented by the exact forms while the field strength's carrier $(1,0)\oplus(0,1)$ is untouched by the shift. The pair of Maxwell equations is the single complex equation $d\mathcal{F}=0$ for $\mathcal{F}=F+i\star F$, whose real part is the Bianchi identity and whose imaginary part is the field equation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $F$ | the field-strength two-form |
| $\star$ | the Hodge dual, $\star(\vec E,\vec B)=(c\vec B,-\vec E/c)$, $\star^{2}=-1$ |
| $\mathcal{F}_{\pm}$ | the self-dual and anti-self-dual halves |
| $\vec N=\vec E+ic\vec B$ | the Riemann–Silberstein vector |
| $\tilde F=i\sqrt{\epsilon}\,\vec N$ | the field-strength biquaternion |
| $\mathrm{Ad}_{\tilde U}$ | the adjoint action, the one the field obeys |

## Further Reading

- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1, Cambridge University Press, 1984 — the self-dual and anti-self-dual decomposition of the field tensor.
- J. D. Jackson, *Classical Electrodynamics*, 3rd ed., Wiley, 1999, chapter 11 — the complex field combination and the duality rotation.
- I. Białynicki-Birula and Z. Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001 — the modern review.
- *The Field-Strength Biquaternion and Its Invariants* — the conventions this article uses throughout.
- *The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Bivector Plane* — the projectors and the naming.
- *Exercise: Duality Rotation and the Riemann–Silberstein Vector* — the duality rotation and the warning about the transformation law.
- *The Two Commuting Complex Triples* — the algebraic reading of the two halves.
