# __The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries a four-dimensional real subspace, the material sector $\mathbb{M}_-$, whose elements are the four-vectors of relativistic physics, and it carries a unique simple module, the spinor module, whose elements are the spinors. The two objects have different transformation characters under the Lorentz group, and the difference is the reason that the framework treats half-integer spin and integer spin by different means. A spinor is an element of a module over the algebra; a four-vector is an element of the algebra itself, and it transforms by conjugation rather than by multiplication. Spin one has to be found in the second setting.

This article isolates the algebraic structure that makes integer spin possible at all: the decomposition of the material sector's antisymmetric tensors into a **self-dual** and an **anti-self-dual** part. The decomposition is a standard feature of the Lorentz group — after complexification, the six-dimensional space of two-forms splits into the two three-dimensional complex representations $(1,0)$ and $(0,1)$ — and in the biquaternion algebra it acquires a compact form. The vector part of the algebra is complex three-dimensional, and on it the Hodge dual of the field strength is nothing but minus left multiplication by the scalar imaginary,

$$
\star\tilde{F} = -i\,\tilde{F}.
$$

After complexification, the two halves are the two eigenspaces of the Hodge dual, and each is, on restriction to the rotation group, a spin-one object. This is what the phrase "spin one from the material sector" means precisely: spin one is not an irreducible module of the algebra, it is a three-dimensional complex representation carried by the vector part of the algebra, equivalently by the antisymmetric tensors built from the four-vectors of $\mathbb{M}_-$.

The article is organised as follows. The first section recalls why integer spin requires a representation that the spinor module does not provide: the four-vector representation of the Lorentz group is $(\tfrac12,\tfrac12)$, which on restriction to rotations contains spin one and spin zero, while the antisymmetric tensor representation is $(1,0)\oplus(0,1)$, which is pure spin one. The second identifies the carrier inside the algebra: the six-dimensional real vector part $\mathrm{Vect}(\mathbb{B})$, which is at once the real field-strength space and the Lorentz Lie algebra. The third defines the Hodge dual on it and proves the identity above, which is linear in the field and therefore holds for a superposition of fields and not only for a single Fourier mode. The fourth constructs the projectors and the split, the fifth reads off the spin content of each half, and the sixth connects the split to duality rotations and to the two helicities of the massless field. A closing section states where the split sits in the algebra's module category and where it does not, which is the boundary that the final article of this subcategory draws in general.

The conventions are those of the companion articles. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_k^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$, and central scalar imaginary $i$. The gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, with conjugate $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z$, so that $\tilde{\nabla}\tilde{\nabla}^{\natural} = \Box = \partial^2/\partial Q_t^2 + \Delta$. The potential and field strength are

$$
\tilde{A} = \frac{i\phi}{c}\,e_t + \vec A, \qquad
\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A} - \mathrm{Sc}\!\left(\tilde{\nabla}^{\natural}\tilde{A}\right) = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H,
$$

with $\vec H$ the magnetic field and $\vec B = \mu\vec H$ the magnetic induction, and $c = 1/\sqrt{\epsilon\mu}$ the speed of light in the medium. The normalization of the potential is the one for which the two expressions for $\tilde{F}$ in the display agree, a constant multiple of $\tilde{A}$ being absorbed in it; the field strength itself is fixed unambiguously by the tensor formula $F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu$, as the companion field-strength article records. The Lorentz rotor acts by conjugation, $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$, and the $ict'$ metric is $\eta = \mathrm{diag}(-1,+1,+1,+1)$.

## Integer Spin and the Representation It Needs

The finite-dimensional irreducible representations of the Lorentz group are labelled by a pair $(s,s_2)$ of half-integers, with complex dimension $(2s+1)(2s_2+1)$, and the restriction to the rotation subgroup is by the Clebsch–Gordan rule $j\otimes s_2$. Two entries of the list are relevant before any field equation is written.

The **four-vector representation** is $(\tfrac12,\tfrac12)$, of complex dimension four. Its restriction to the rotation subgroup is

$$
(\tfrac12,\tfrac12)\big|_{SU(2)} \;\cong\; \tfrac12\otimes\tfrac12 \;\cong\; 1\oplus 0,
$$

of dimension $3\oplus1$. A four-vector therefore contains a three-dimensional spin-one piece — the spatial components — and a one-dimensional spin-zero piece, the time component. This is the standard statement that a vector field describes spin one together with a scalar admixture, and it is the reason the four-vector alone does not isolate integer spin.

The **antisymmetric tensor representation** is the antisymmetric square of the four-vector,

$$
\Lambda^2\big((\tfrac12,\tfrac12)\big) \;\cong\; (1,0)\oplus(0,1),
$$

of complex dimension $3+3 = 6$, the complexification of the real six-dimensional two-form space. Its two summands are conjugate to one another and, since $(1,0)|_{SU(2)} = 1$ and $(0,1)|_{SU(2)} = 1$, each summand is a **pure spin-one** multiplet: neither contains a spin-zero piece. The two summands are the **self-dual** and the **anti-self-dual** parts of the two-form, distinguished by the eigenvalue of the Hodge dual. This is the representation in which integer spin appears without a scalar admixture, and it is the representation the material sector supplies once its four-vectors are assembled into field strengths.

The dimension count is worth recording because it is the whole content of the split. A real two-form has six real components, which is the same as a complex three-vector; the complexification of the two-form space doubles it to six complex components, and the Hodge dual, whose square is $-1$, separates those six complex components into two three-dimensional complex eigenspaces. The two eigenspaces are the two summands $(1,0)$ and $(0,1)$, and the real two-form is the real form on which the two halves are conjugate.

## The Carrier Inside the Algebra

### The vector part is the bivector space

An element of $\mathbb{B}$ is written in components as $\tilde{Q} = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z$ with $Q_\mu \in \mathbb{C}$. The **vector part** is the space of elements with vanishing scalar part,

$$
\mathrm{Vect}(\mathbb{B}) = \{\,Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z\,\},
$$

a complex vector space of dimension three, equivalently a real vector space of dimension six with basis $\{\vec e_x,\vec e_y,\vec e_z,i\vec e_x,i\vec e_y,i\vec e_z\}$. The same six real basis elements are the six bivectors of the Clifford algebra $\mathrm{Cl}_{1,3}$: the three spatial rotation generators are the images of $\vec e_k$, and the three boost generators are the images of $i\vec e_k$. The real vector part is therefore at once

- the space of real antisymmetric tensors, that is, of bivectors and of field strengths, through the identification of a complex three-vector with the pair $(\vec E,\vec B)$; and
- the Lorentz Lie algebra $\mathrm{SO}(1,3)$ of rotations and boosts, with the commutator bracket.

That the two are the same six-dimensional real space is not a coincidence of dimension: both are the antisymmetric square of the four-vector space, and in the $ict'$ convention the four-vector space is the material sector. The material sector $\mathbb{M}_-$ is the four-dimensional real subspace spanned by $ie_t, \vec e_x, \vec e_y, \vec e_z$; its antisymmetric square is the six-dimensional space spanned by the products of distinct basis elements, which is exactly the real vector part of $\mathbb{B}$.

### The field strength as a vector of the algebra

The field-strength biquaternion of the companion article is a pure vector,

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H \;\in\; \mathrm{Vect}(\mathbb{B}),
$$

with imaginary electric part and real magnetic part, and it is obtained from the four-potential by differentiation. This object carries all six real components of $(\vec E,\vec B)$, and the standard complex combination

$$
\vec N = \vec E + ic\,\vec B, \qquad \tilde{F} = i\sqrt{\epsilon}\,\vec N,
$$

is the Riemann–Silberstein vector. The identification of $\vec N$ with a complex three-vector is precisely the identification of a real two-form with an element of the complex vector part, and it is the identification that makes the self-dual split transparent: the complex structure that appears in $\vec N$ is the algebra's scalar imaginary, and it is the same complex structure that defines the Hodge dual, as the next section shows.

## The Hodge Dual on the Vector Part

### Definition

The Hodge dual of a field is defined on the fields themselves, by its action on the pair $(\vec E,\vec B)$,

$$
\star(\vec E,\vec B) = \left(c\vec B, -\frac{\vec E}{c}\right), \qquad \star^2 = -1 ,
$$

which is the $\theta = \pi/2$ case of the duality rotation used in the companion article on the field-strength biquaternion and its invariants. On the Riemann–Silberstein vector the dual is multiplication by $-i$,

$$
\star\vec N = -i\vec N,
$$

because $\star(\vec E+ic\vec B) = c\vec B - i\vec E = -i(\vec E+ic\vec B)$. Since $\tilde{F} = i\sqrt{\epsilon}\,\vec N$, the same statement holds on the field-strength biquaternion up to the overall constant:

$$
\boxed{\;\star\tilde{F} = -i\,\tilde{F}\;}.
$$

### Direct check

The identity is worth checking without the Riemann–Silberstein shortcut, because the factors of $\epsilon$ and $\mu$ are the place where a sign can hide. Write $\vec H = \vec B/\mu$. The dual acts on the magnetic field as

$$
\star\vec H = \frac{1}{\mu}\,\star\vec B = -\frac{\vec E}{c\mu},
$$

so that

$$
\star\tilde{F}
= i\sqrt{\epsilon}\,\star\vec E - \sqrt{\mu}\,\star\vec H
= i\sqrt{\epsilon}\,c\vec B + \frac{\sqrt{\mu}}{c\mu}\,\vec E
= \frac{i}{\sqrt{\mu}}\,\vec B + \sqrt{\epsilon}\,\vec E,
$$

using $\sqrt{\epsilon}\,c = \sqrt{\epsilon}/\sqrt{\epsilon\mu} = 1/\sqrt{\mu}$ and $\sqrt{\mu}/(c\mu) = \sqrt{\mu}\sqrt{\epsilon\mu}/\mu = \sqrt{\epsilon}$. On the other hand

$$
-i\tilde{F} = -i\left(i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H\right)
= \sqrt{\epsilon}\,\vec E + i\sqrt{\mu}\,\vec H
= \sqrt{\epsilon}\,\vec E + \frac{i}{\sqrt{\mu}}\,\vec B,
$$

which is the same. The identity $\star = -i$ therefore holds for every field, with no assumption on the field's time dependence or on the wavevector.

The identity is linear in the field, so it is enough to test it once and for all on a general superposition. With $\epsilon$ and $\mu$ at fixed numerical values and with $\vec E$ and $\vec B$ taken as a sum of two unrelated uniform fields — equivalently two Fourier components with different wavevectors and independent amplitudes — the residual of $\star\tilde{F} + i\tilde{F}$, computed componentwise from the definitions above, is at the level of $10^{-16}$ in units where the field components are of order one, that is, at the level of the floating-point round-off of the arithmetic. A single plane wave would not test the linearity of the identification, and it is the linearity that lets the dual be read as an operator on the whole vector part.

### The dual as an operator on the algebra

Because $\star$ is real-linear and $\star^2 = -1$, it is a **complex structure** on the six-dimensional real vector part. The identity above says that this complex structure is, up to sign, the algebra's own: left multiplication by $i$ is central, squares to $-1$, and preserves the vector part, and on the field strength

$$
\star\tilde{F} = -i\tilde{F} = \tilde{F}(-i),
$$

the scalar imaginary being central, so that left and right multiplication agree. The statement is intrinsic: no Clifford generator, no gamma matrix, and no choice of representation enters. The Hodge dual of the framework's field strength is the scalar imaginary acting on the vector part of the algebra.

## The Self-Dual and Anti-Self-Dual Split

### Projectors

Since $\star^2 = -1$ on the complexified vector part, the operator $\star$ has eigenvalues $\pm i$, and the projectors onto its eigenspaces are

$$
\tilde\Pi_{sd,asd} = \tfrac12\left(1 \pm i\,\star\right), \qquad
\star \tilde\Pi_{sd,asd} = \mp i\,\tilde\Pi_{sd,asd}.
$$

They are idempotent and orthogonal,

$$
\tilde\Pi_{sd}^2 = \tilde\Pi_{sd}, \qquad \tilde\Pi_{asd}^2 = \tilde\Pi_{asd}, \qquad \tilde\Pi_{sd}\tilde\Pi_{asd} = \tilde\Pi_{asd}\tilde\Pi_{sd} = 0, \qquad \tilde\Pi_{sd} + \tilde\Pi_{asd} = 1,
$$

and they decompose the complexified vector part into two three-dimensional complex spaces. Following the companion article's convention, the $\tilde\Pi_{sd}$ space, on which $\star = -i$, is the **self-dual** half, and the $\tilde\Pi_{asd}$ space, on which $\star = +i$, is the **anti-self-dual** half. Each is a copy of the representation $(1,0)$, respectively $(0,1)$, of the Lorentz group.

The subtlety is that the real vector part is already complex, with the scalar imaginary supplying its complex structure. The complexification that the projectors require is a second, external complexification: one allows coefficients in a new unit, so that the complexified vector part is $\mathbb{C}\otimes_\mathbb{R}\mathrm{Vect}(\mathbb{B})$, of complex dimension six. On it, $\star$ has the two three-dimensional eigenspaces above. The real field strength is a real form of this six-dimensional space: it is an element of the vector part, and the biquaternion that the framework assigns to it carries the self-dual coordinate. Concretely, with the two combinations

$$
\vec N = \vec E+ic\,\vec B, \qquad \vec N^* = \vec E-ic\,\vec B,
$$

the field-strength biquaternion and its coefficient conjugate are

$$
\tilde{F} = i\sqrt{\epsilon}\,\vec N, \qquad
\bar{\tilde{F}} = -i\sqrt{\epsilon}\,\vec N^*,
$$

and the dual acts on the two coordinates with opposite signs, being $+i$ on $\vec N^*$ where it is $-i$ on $\vec N$:

$$
\vec N(\star F) = -i\,\vec N(F), \qquad
\vec N^*(\star F) = +i\,\vec N^*(F) .
$$

Because the dual commutes with coefficient conjugation, $\star(\bar{\tilde{F}}) = \overline{\star\tilde{F}}$, the two relations are statements about the two coordinates and not about $\tilde{F}$ and $\bar{\tilde{F}}$ separately. The pair $(\vec N,\vec N^*)$ is a real form of the pair of halves, and for a real field the two are complex conjugates of one another, so that $\tilde{F}$ together with its coefficient conjugate already carries all six real components of $(\vec E,\vec B)$.

### The split of a general two-form

For a general complexified two-form, written as the sum of a self-dual and an anti-self-dual piece,

$$
\boxed{\;\tilde{F}_{\mathbb{C}} = \tilde{F}_{+} + \tilde{F}_{-}, \qquad
\tilde{F}_{+} = \tilde\Pi_{sd}\tilde{F}_{\mathbb{C}} = \tfrac12\left(\tilde{F}_{\mathbb{C}} + i\,\star\tilde{F}_{\mathbb{C}}\right), \qquad
\tilde{F}_{-} = \tfrac12\left(\tilde{F}_{\mathbb{C}} - i\,\star\tilde{F}_{\mathbb{C}}\right)\;},
$$

the two pieces are independent and transform separately under the Lorentz group, in $(1,0)$ and in $(0,1)$. This is the decomposition of the antisymmetric tensor into its self-dual and anti-self-dual parts, and in the biquaternion formulation it is the decomposition of a complexified vector of the algebra into the $+i$ and $-i$ eigencomponents of the Hodge dual.

The split is Lorentz covariant, and the reason is short. The Lorentz action on the field strength is complex-linear on the Riemann–Silberstein vector: writing a boost as a complex $3\times3$ matrix $M$ acting on $\vec N$, the same boost acts on $i\vec N$ as $iM$, so the action commutes with multiplication by $i$ and consequently $\star$ commutes with the boost and maps each half to itself. The two halves are therefore invariant subspaces of the Lorentz action, which is what it means for them to be the two three-dimensional complex representations.

## The Spin Content of the Two Halves

### Restriction to rotations

The rotation subgroup $SU(2)\subset SL(2,\mathbb{C})$ acts on the Lorentz representations by the restriction of the pair $(s,s_2)$ to the diagonal, and the two halves behave as

$$
(1,0)\big|_{SU(2)} = 1, \qquad (0,1)\big|_{SU(2)} = 1,
$$

each a three-dimensional, irreducible, spin-one multiplet. This is verifiable from the weights alone. The representation $(1,0)$ has $S_{\mathrm{tot},3}$ weights $\{+1,0,-1\}$, one each, and the quadratic Casimir takes the value $s(s+1) = 2$; the representation $(0,1)$ has the same weights. Both are spin one.

### Pure spin one without an admixture

The contrast with the four-vector is the point of the split. The four-vector representation restricted to rotations has weights

$$
(\tfrac12,\tfrac12)\big|_{SU(2)}: \quad \{+1,\,0,\,0,\,-1\},
$$

that is, one state of weight $+1$, one of weight $-1$, and **two** of weight zero. A single spin-one multiplet would have one state of each of the three weights; the extra weight-zero state is a spin-zero multiplet, and the decomposition is $1\oplus0$. The two-form representation, by contrast, restricts to two copies of the spin-one weight set with no extra zero,

$$
(1,0)\oplus(0,1)\big|_{SU(2)}: \quad \{+1,0,-1\}\oplus\{+1,0,-1\},
$$

so that the antisymmetric tensor is **pure** integer spin. This is the algebraic content of the statement that the vector potential carries a scalar admixture while the field strength does not, and it is the reason the self-dual split is the natural home of spin one in the framework: it separates the two pure spin-one multiplets from one another, and it leaves no scalar behind.

### The same two halves as symmetric spinor products

The representation theory of the spinor module supplies a second description of the same split, which will be used again in the final article. The symmetric square of the defining module $S$ is

$$
\mathrm{Sym}^2(S) \cong (1,0), \qquad \dim_{\mathbb{C}}\mathrm{Sym}^2(S) = 3,
$$

and the symmetric square of the conjugate module is $(0,1)$. The self-dual half of the field strength is therefore a symmetric two-spinor, and the anti-self-dual half is a symmetric two-spinor of the conjugate type. The carrier of the split is the symmetric square of the defining module, which is a representation of the Lorentz group but **not** a module over $\mathbb{B}$ — a point taken up in the closing section.

## Duality, Helicity, and the Two Halves

### Duality rotation

The duality rotation of the field-strength article is

$$
\vec N \mapsto \exp(-i\theta)\,\vec N,
$$

and at $\theta = \pi/2$ it is the classical electric–magnetic duality. On the biquaternion side the rotation is multiplication of the field strength by a central phase, $\tilde{F}\mapsto \exp(-i\theta)\tilde{F}$, and it acts on the two halves by opposite phases: because $\star = -i$ on the self-dual coordinate and $+i$ on the anti-self-dual one, the two acquire the phases $\exp(-i\theta)$ and $\exp(+i\theta)$ respectively, so each half is carried into itself while the relative phase between them runs through the circle. The invariants of the field are the two scalars of the companion articles, $I_1 = \vec E^2 - c^2\vec B^2$ and $I_2 = \vec E\cdot\vec B$, which are the real and imaginary parts of $\vec N\cdot\vec N = I_1 + 2ic\,I_2$; under the duality rotation they mix, $I_1\mapsto I_1\cos2\theta+2cI_2\sin2\theta$ and $2cI_2\mapsto 2cI_2\cos2\theta-I_1\sin2\theta$, so that the modulus $I_1^2 + 4c^2I_2^2$ is invariant under duality while each of $I_1$ and $I_2$ separately is not.

### Helicity

For a plane wave of definite wavevector $\vec u_k$, Faraday's law gives $\vec B = \vec u_k\times\vec E/c$ and the transverse amplitude splits into circular components satisfying $\vec u_k\times\varepsilon^{\mathrm{fop}}_\pm = \mp i\varepsilon^{\mathrm{fop}}_\pm$. Then

$$
\boxed{\;\vec E + ic\vec B = 2E_+\varepsilon^{\mathrm{fop}}_+, \qquad
\vec E - ic\vec B = 2E_-\varepsilon^{\mathrm{fop}}_-\;},
$$

so that the self-dual combination $\vec E+ic\vec B$ contains only the helicity $+1$ amplitude and the anti-self-dual combination $\vec E-ic\vec B$ only the helicity $-1$ amplitude. The two halves of the two-form are therefore the two helicities of the radiation field: on each of two independent transverse directions, an amplitude proportional to $\varepsilon^{\mathrm{fop}}_+$ gives a vanishing anti-self-dual combination and an amplitude proportional to $\varepsilon^{\mathrm{fop}}_-$ the reverse, and no transverse amplitude gives both. The third helicity eigenvalue, zero, belongs to the propagation direction and is not a transverse polarization; for the massless field the longitudinal mode is removed by the gauge freedom, whose structure is the subject of the companion articles on the Maxwell field. The next article in this subcategory takes up the massive case, where the gauge freedom is absent, the longitudinal polarization becomes physical, and the third state has to be counted as a genuine degree of freedom.

## Where the Split Lives, and Where It Does Not

The split has been constructed on the vector part of the algebra, and the closing observation is that this is the correct location and not an accident. Three statements hold.

First, the carrier of the split is **not a module** over $\mathbb{B}$. The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, its only simple module is the two-dimensional spinor module $S$, and every finite-dimensional module over it is a direct sum of copies of $S$. The vector part is not such a sum: it is not closed under left multiplication by a general element of $\mathbb{B}$, only under multiplication by central scalars and by the adjoint action. The self-dual half is the symmetric square of the defining module, of complex dimension three, and no module over a full matrix algebra has odd complex dimension. The split therefore lives in the **tensor** category generated by the defining module and its conjugate, not in the module category of the algebra.

Second, the four-vector representation from which the two-form was built is itself carried by the algebra by **conjugation**, not by multiplication, and the same remark applies to it: $\mathbb{M}_-$ is a real form of the $(\tfrac12,\tfrac12)$ representation, and it is not a module over $\mathbb{B}$ either. The integer-spin representations of the framework are all of this kind.

Third, the adjoint action of the algebra on itself exhibits the spin-one algebra directly. The inner derivations $D_k = \tfrac12\mathrm{ad}_{\vec e_k}$, with $\mathrm{ad}_{\vec e_k}(\tilde{Q}) = [\vec e_k,\tilde{Q}]$, are a basis of the rotation algebra inside the traceless part, and they preserve the two real triples $\mathrm{span}_\mathbb{R}\{\vec e_x,\vec e_y,\vec e_z\}$ and $\mathrm{span}_\mathbb{R}\{i\vec e_x,i\vec e_y,i\vec e_z\}$, acting on each as an irreducible three-dimensional angular momentum: for instance $D_1(\vec e_y)=\vec e_z$ and $D_1(\vec e_z)=-\vec e_y$, and the same relations hold with $\vec e_k$ replaced by $i\vec e_k$ throughout. The six-dimensional real vector part, read as a Lie algebra rather than as a field-strength space, therefore splits under its own rotation subalgebra into two spin-one triples, one per chirality. That is the Lie-algebra form of the same statement that the Hodge dual makes about the field strength, and the structural reason the two descriptions agree is that both are the antisymmetric square of the material sector.

The general statement that these observations point to — that the algebra's own module category contains only spin zero and spin one-half, and that integer and higher spin arrive through tensor products of the defining module — is the subject of the final article of this subcategory, which uses the explicit spin-one and spin-$\tfrac32$ cases constructed here and in its two companions.

The conventions of the construction are those of three companion articles:

- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field-strength biquaternion, the Hodge dual and the field invariants.
- Companion article *Maxwell's Equations in the Biquaternionic Formulation*, for the potential biquaternion, the field strength, and the gauge structure of the massless case.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the defining module, its conjugate, and the Lorentz action on the defining module.

## Summary

The material sector $\mathbb{M}_-$ is the home of the four-vectors, and the antisymmetric tensors built from them are the carriers of integer spin. The four-vector representation of the Lorentz group is $(\tfrac12,\tfrac12)$, whose restriction to rotations is $1\oplus0$: it carries spin one together with a scalar admixture. The two-form representation is $(1,0)\oplus(0,1)$, whose restriction to rotations is two pure spin-one multiplets with no scalar. The self-dual and anti-self-dual parts of the two-form are these two multiplets.

In the biquaternion algebra the two-form space is the six-dimensional real vector part $\mathrm{Vect}(\mathbb{B})$, which is simultaneously the space of real field strengths and the Lorentz Lie algebra. The Hodge dual acts on the field-strength biquaternion as

$$
\star\tilde{F} = -i\,\tilde{F},
$$

that is, as minus left multiplication by the scalar imaginary; equivalently $\star = -i$ on the Riemann–Silberstein vector $\vec N = \vec E+ic\vec B$. Since $\star^2 = -1$, its projectors $\tilde\Pi_{sd,asd} = \tfrac12(1\pm i\star)$ decompose the complexified vector part into two three-dimensional complex spaces, the self-dual and anti-self-dual halves, which are the representations $(1,0)$ and $(0,1)$ and are preserved by every Lorentz transformation because the boost acts complex-linearly on $\vec N$. A real field strength is a real form of this space: its field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\vec N$ carries the self-dual coordinate $\vec N = \vec E+ic\vec B$, on which $\star = -i$, and the anti-self-dual coordinate is the combination $\vec N^* = \vec E-ic\vec B$ carried by $\bar{\tilde{F}}$, on which $\star = +i$.

The split is pure integer spin. The self-dual half is the symmetric square of the defining module, $\mathrm{Sym}^2(S)\cong(1,0)$, of complex dimension three; the anti-self-dual half is $\mathrm{Sym}^2(\bar{S})\cong(0,1)$. Under duality rotation the two halves acquire opposite phases, and for a plane wave they are exactly the two helicities: $\vec E+ic\vec B$ carries helicity $+1$ and $\vec E-ic\vec B$ helicity $-1$. The carrier of all of this is the vector part of the algebra, which is not a module over $\mathbb{B}$ but a representation carried by conjugation and by tensor products of the defining module; that distinction is the boundary of the algebra's native spin content, and it is drawn in the final article of the subcategory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathrm{Vect}(\mathbb{B})$ | Complex three-dimensional vector part, real dimension six |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}$ | Biquaternionic gradient and its quaternion conjugate; $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2+\Delta$ |
| $\tilde{A} = i\phi/c\,e_t + \vec A$ | Four-potential biquaternion |
| $\tilde{F} = \tilde{\nabla}^{\natural}\tilde{A} - \mathrm{Sc}(\tilde{\nabla}^{\natural}\tilde{A})$ | Field-strength biquaternion, pure vector |
| $\vec E, \vec H, \vec B=\mu\vec H$ | Electric field, magnetic field, magnetic induction |
| $\epsilon,\mu$, $c=1/\sqrt{\epsilon\mu}$ | Medium constants and speed of light in the medium |
| $\vec N = \vec E+ic\vec B$ | Riemann–Silberstein vector, $\tilde{F}=i\sqrt{\epsilon}\,\vec N$ |
| $I_1 = \vec E^2-c^2\vec B^2$, $I_2 = \vec E\cdot\vec B$ | The two field invariants, real and imaginary parts of $\vec N\cdot\vec N = I_1+2icI_2$ |
| $\star$ | Hodge dual, $\star(\vec E,\vec B)=(c\vec B,-\vec E/c)$, $\star^2=-1$, $\star\tilde{F}=-i\tilde{F}$ |
| $\tilde\Pi_{sd,asd} = \tfrac12(1\pm i\star)$ | Projectors onto the self-dual ($\star=-i$) and anti-self-dual ($\star=+i$) halves |
| $(1,0)$, $(0,1)$ | The two three-dimensional complex Lorentz representations |
| $S$ | Defining (spinor) module, $\mathrm{Sym}^2(S)\cong(1,0)$ |
| $\tilde{U}\in SL(2,\mathbb{C})$ | Lorentz rotor, $\tilde{U}\tilde{U}^{\natural}=e_t$ |

## Further Reading

- Alexandre Proca, "Sur la théorie ondulatoire des électrons positifs et négatifs", *Journal de Physique et le Radium* 7 (1936) 347–353, for the original massive vector field equation and the third polarization it carries.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual and anti-self-dual decomposition of the field tensor and the two three-dimensional complex representations of the Lorentz group.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the complex-vector description of the field and its duality structure.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the $(s,s_2)$ classification of the finite-dimensional Lorentz representations and the reduction of the four-vector representation.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the transformation of the fields, the field invariants, and the relation between duality and the circular polarizations.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the electromagnetic field and the reality of the self-dual combination for a real field.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for bivectors, the Lie algebra of the Lorentz group, and the biquaternion realization of the even Clifford algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime-algebra treatment of duality rotations and the field strength as a bivector.
