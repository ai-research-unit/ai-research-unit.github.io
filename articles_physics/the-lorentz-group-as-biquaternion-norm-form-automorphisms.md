# __The Lorentz Group as Biquaternion Norm-Form Automorphisms__

## Introduction

The group that acts on the material sector of the biquaternion framework has so far been introduced in two ways: as the group of unit-norm biquaternions, and as the group of rotor conjugations they generate. Both descriptions take the group as given and derive its action. This article takes the opposite route. It asks what group the algebra *forces* when the norm form is regarded as the structure to be preserved, and shows that the answer is the Lorentz group, with the rotor description recovered as the coordinate form of the automorphisms.

The point of the automorphism reading is that the norm form is not an extra structure laid on the algebra. It is the algebra's own multiplicative quadratic form,

$$
N(\tilde{Q}) = \tilde{Q}\overline{\tilde{Q}} = \sum_{\mu=0}^{3}Q_\mu^2,
$$

and it satisfies

$$
N(\tilde{Q}\tilde{R}) = N(\tilde{Q})\,N(\tilde{R})
$$

for all biquaternions $\tilde{Q},\tilde{R}$. A multiplicative quadratic form on a four-dimensional algebra is a rare object, and the group that preserves it is thereby tied to the algebra's multiplication rather than imposed from outside. The automorphism group of the form on the complex algebra is $O(4,\mathbb{C})$; the automorphisms that also preserve the algebra's **real structure** — the anti-Hermitian material slice — form the Lorentz group.

Three statements organize the article, and they are the three levels at which the identification can be read.

- **At the complex level**, $N$ is a nondegenerate symmetric form on $\mathbb{B}\cong\mathbb{C}^4$, and the automorphism group is the complex orthogonal group $O(4,\mathbb{C})$. Via the determinant realization $N=\det$, the connected component is $SO(4,\mathbb{C})\cong(SL(2,\mathbb{C})\times SL(2,\mathbb{C}))/\{\pm(e_0,e_0)\}$, acting by $\tilde{X}\mapsto\tilde{A}\tilde{X}\tilde{B}^{-1}$.
- **At the real level**, the restricted form on the anti-Hermitian slice is the Minkowski form $\eta = \mathrm{diag}(-1,+1,+1,+1)$, and the automorphisms preserving the slice are the real orthogonal maps of signature $(3,1)$, with identity component the restricted Lorentz group $SO^+(1,3)$.
- **At the rotor level**, the identity component is exactly the group of conjugations $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ by unit-norm biquaternions, and the correspondence is two-to-one.

**Boundaries.** This is a group-theoretic and geometric article. The spinor module, its one-sided action, and the representation theory of the group belong to the sibling category on relativistic quantum theory and to the companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; they are not developed here. The topology of the cover, and the composition law of boosts in detail, belong to the companion article *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*. The structure and the finite-dimensional representations of the group as such are treated in *The Lorentz Group in Biquaternionic Form — Structure and Representations*; this article's subject is the characterization of the group by the form.

**Conventions.** We use those of the read list unchanged. The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with quaternion basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$ and $e_je_k = -\delta_{jk}e_0 + \varepsilon_{jkl}e_l$, and central scalar imaginary $i$. The subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector — the material sector), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector — the informational sector), $\mathbb{H}_{\mathbb{B}}$ (real quaternions) and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_\mathbb{R}\{e_0, ie_0\}$ (the center). The conjugations are $\bar{\cdot}$ (quaternion), ${}^*$ (complex), ${}^\dagger = \bar{\cdot}^{\,*}$ (Hermitian) and ${}^\flat = -\dagger$ (anti-Hermitian). The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ — level 1, the identity $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{C}$ — and its restriction to the real material slice is the level-2 form $\eta = \mathrm{diag}(-1,+1,+1,+1)$. The matrix realization is $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ with $\Phi(e_0) = I_2$, $\Phi(e_k) = -i\sigma_k$, $\Phi(i) = iI_2$. The material coordinate is $\tilde{X} = ict\,e_0 + \mathbf{x}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. The trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## The Norm Form as a Quadratic Form

The norm form is the quadratic map

$$
N:\ \mathbb{B}\longrightarrow\mathbb{C},
\qquad
N(\tilde{Q}) = \tilde{Q}\overline{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 ,
$$

whose polarization is the symmetric bilinear form

$$
B(\tilde{Q},\tilde{R}) = \tfrac12\left[N(\tilde{Q}+\tilde{R}) - N(\tilde{Q}) - N(\tilde{R})\right]
= Q_0R_0 + Q_1R_1 + Q_2R_2 + Q_3R_3 .
$$

In the coordinate basis $(e_0,e_1,e_2,e_3)$ its matrix is the identity,

$$
B(\tilde{Q},\tilde{R}) = \sum_\mu Q_\mu R_\mu ,
\qquad
G = \mathrm{diag}(+1,+1,+1,+1) ,
$$

so $N$ is a **nondegenerate complex quadratic form of maximal Witt index** on $\mathbb{C}^4$. It is not positive definite over $\mathbb{C}$ — no complex form is — and it is isotropic: it has nonzero null vectors, which are the zero divisors of the companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*.

Two properties make $N$ the algebra's own form rather than a form on a vector space.

**Multiplicativity.** For all $\tilde{Q},\tilde{R}$,

$$
N(\tilde{Q}\tilde{R})
= \tilde{Q}\tilde{R}\,\overline{\tilde{Q}\tilde{R}}
= \tilde{Q}\tilde{R}\,\overline{\tilde{R}}\,\overline{\tilde{Q}}
= \tilde{Q}\,N(\tilde{R})\,\overline{\tilde{Q}}
= N(\tilde{R})\,\tilde{Q}\overline{\tilde{Q}}
= N(\tilde{Q})\,N(\tilde{R}),
$$

where the fourth equality uses that $N(\tilde{R})$ is a complex scalar and therefore central in $\mathbb{B}$. The norm form is a **homomorphism of multiplicative monoids** from $(\mathbb{B},\cdot)$ to $(\mathbb{C},\cdot)$.

**Compatibility with the real structure.** The conjugations act on the form by

$$
N(\tilde{Q}^\dagger) = \overline{N(\tilde{Q})} = N(\tilde{Q})^{*},
\qquad
N(\bar{\tilde{Q}}) = N(\tilde{Q}),
$$

so the form is real on the Hermitian and anti-Hermitian slices. This is what will allow the complex form to restrict to a real form of Minkowski signature.

**Automorphisms of the form.** An automorphism of $(\mathbb{B},N)$ is an invertible $\mathbb{C}$-linear map $T$ with

$$
N(T\tilde{Q}) = N(\tilde{Q})
\qquad\text{for all }\tilde{Q}\in\mathbb{B}.
$$

Since $N$ is nondegenerate with matrix the identity, the group of such maps is the complex orthogonal group

$$
O(4,\mathbb{C}) = \{\,T\in GL_4(\mathbb{C}) : T^{T}T = I_4\,\},
$$

of complex dimension six, with connected component $SO(4,\mathbb{C}) = O(4,\mathbb{C})\cap SL_4(\mathbb{C})$. This is the largest group the form alone defines. The Lorentz group will be a real form of it, selected by the requirement that the real structure of the algebra be preserved.

## The Determinant Realization and the Complex Group

The matrix realization makes the form and its automorphisms concrete. With $\Phi$ as in the conventions,

$$
\Phi(\tilde{Q}) =
\begin{pmatrix}
Q_0 - iQ_3 & -iQ_1 - Q_2\\
-iQ_1 + Q_2 & Q_0 + iQ_3
\end{pmatrix},
\qquad
\det\Phi(\tilde{Q}) = Q_0^2+Q_1^2+Q_2^2+Q_3^2 = N(\tilde{Q}).
$$

The norm form **is the determinant**, and $\Phi$ is an isomorphism of $\mathbb{C}$-algebras. The verification of the determinant identity is a direct expansion; it was also checked numerically on random biquaternions, with $\det\Phi(\tilde{Q})$ and $N(\tilde{Q})$ agreeing to machine precision.

The determinant is a quadratic form on the four-dimensional space $M_2(\mathbb{C})$, and its automorphism group is classical. Consider the map

$$
T_{\tilde{A},\tilde{B}}:\ \tilde{X}\ \longmapsto\ \tilde{A}\,\tilde{X}\,\tilde{B}^{-1},
\qquad
\tilde{A},\tilde{B}\in GL_2(\mathbb{C}).
$$

It is invertible and $\mathbb{C}$-linear, and its effect on the form is

$$
N(T_{\tilde{A},\tilde{B}}\tilde{X}) = \det\!\left(\tilde{A}\tilde{X}\tilde{B}^{-1}\right)
= \frac{\det\tilde{A}}{\det\tilde{B}}\,\det\tilde{X}
= \frac{\det\tilde{A}}{\det\tilde{B}}\,N(\tilde{X}).
$$

Preservation of $N$ therefore requires $\det\tilde{A} = \det\tilde{B}$, and one may normalize both to unit determinant; the surviving pairs are $(\tilde{A},\tilde{B})\in SL(2,\mathbb{C})\times SL(2,\mathbb{C})$. The kernel of the assignment $(\tilde{A},\tilde{B})\mapsto T_{\tilde{A},\tilde{B}}$ is the set of pairs acting trivially, $T_{\tilde{A},\tilde{B}} = \mathrm{id}$, which is

$$
\ker = \{\,(\lambda I_2,\lambda I_2) : \lambda\in\mathbb{C}^\times\,\},
\qquad
\lambda^2 = 1 \ \text{ under the determinant normalization},
\qquad
\ker = \{\pm(e_0,e_0)\} .
$$

Hence

$$
\boxed{\; SO(4,\mathbb{C}) \;\cong\; \frac{SL(2,\mathbb{C})\times SL(2,\mathbb{C})}{\{\pm(e_0,e_0)\}} \;}
\qquad
\text{(complex dimension 3 + 3 = 6).}
$$

The two factors are the two chiral halves of the complexified rotation group; in the algebra they correspond to left and right multiplication. This is the complex group of the norm form. It is not the Lorentz group: it acts on the complexified four-vector space, and its two $SL(2,\mathbb{C})$ factors are independent.

## The Real Slice and the Minkowski Form

The Lorentz group is selected by the algebra's real structure. The **anti-Hermitian slice** is

$$
\mathbb{M}_- = \{\tilde{X}\in\mathbb{B} : \tilde{X}^\dagger = -\tilde{X}\},
$$

a four-**real**-dimensional subspace, with the real basis $\{ie_0, e_1, e_2, e_3\}$. Writing

$$
\tilde{X} = i x_0 e_0 + x_1e_1 + x_2e_2 + x_3e_3,
\qquad x_\mu\in\mathbb{R},
$$

the norm form is real and indefinite:

$$
N(\tilde{X}) = (ix_0)^2 + x_1^2 + x_2^2 + x_3^2 = -x_0^2 + \mathbf{x}^2 .
$$

The restriction of $N$ to $\mathbb{M}_-$, in the real coordinates, is therefore the quadratic form with matrix

$$
\eta = \mathrm{diag}(-1,+1,+1,+1),
$$

the level-2 Minkowski form of the series. Identifying $x_0 = ct$, it is the interval. The same computation on the other distinguished slices gives the full picture of the form's real restrictions:

| Slice | General element | $N$ | Signature |
|---|---|---|---|
| $\mathbb{H}_{\mathbb{B}}$ | $a_0e_0 + \mathbf{a}$, $a_\mu\in\mathbb{R}$ | $a_0^2+\mathbf{a}^2$ | $(4,0)$, positive definite |
| $i\mathbb{H}_{\mathbb{B}}$ | $i(a_0e_0+\mathbf{a})$ | $-(a_0^2+\mathbf{a}^2)$ | $(0,4)$, negative definite |
| $\mathbb{M}_-$ | $ix_0e_0+\mathbf{x}$ | $-x_0^2+\mathbf{x}^2$ | $(3,1)$, timelike $x_0$ direction |
| $\mathbb{M}_+$ | $q_0e_0+i\mathbf{q}$ | $q_0^2-\mathbf{q}^2$ | $(1,3)$, the mirror of $\mathbb{M}_-$ |

The complex form $\mathrm{diag}(+1,+1,+1,+1)$ has real forms of both signatures; the two Hermitian-type slices carry the Minkowski real form, the real-quaternion slice the Euclidean one, and the two are exchanged by multiplication by $i$. The physical slice is $\mathbb{M}_-$.

The real structure is not decoration: it is what tells the complex group which real form of the algebra is physical. A $\mathbb{C}$-linear automorphism of the complexification need not map $\mathbb{M}_-$ to itself. The automorphisms that do are the ones the physical theory uses.

## The Lorentz Group as the Automorphisms of the Slice

Consider the automorphisms of $N$ that preserve the real slice:

$$
\mathcal{G} = \{\,T\in O(4,\mathbb{C}) : T(\mathbb{M}_-)\subseteq\mathbb{M}_-\,\}.
$$

On $\mathbb{M}_-$ the map $T$ is a real-linear transformation, and the condition

$$
N(T\tilde{X}) = N(\tilde{X})\ \text{ for all }\tilde{X}\in\mathbb{M}_-
$$

says exactly that $T$ preserves the Minkowski form $\eta = \mathrm{diag}(-1,+1,+1,+1)$. Hence

$$
\mathcal{G} \;\cong\; O(1,3),
$$

the full Lorentz group including the discrete reflections and the time-reversal and parity components. The connected component of the identity is the **restricted Lorentz group** $SO^+(1,3)$: the transformations that are proper (determinant $+1$) and orthochronous (preserve the time direction). This is the group the algebra supplies at the real level: the automorphisms of the norm form that respect the material slice.

The discrete components are automorphisms of the form and are not rotor conjugations; they include spatial reflection and time reversal, which are outer with respect to the rotor group. The rotor group covers only the identity component, which is why a spinor or a rotor is not by itself sensitive to orientation-reversing transformations.

## The Rotor Realization of the Automorphisms

The identity component has an explicit algebraic form. A **Lorentz rotor** is a unit-norm biquaternion,

$$
\tilde{\Lambda}\in\mathbb{B},
\qquad
\tilde{\Lambda}\overline{\tilde{\Lambda}} = e_0 ,
$$

and it acts by **conjugation**,

$$
\pi(\tilde{\Lambda}):\ \tilde{X}\ \longmapsto\ \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^\dagger .
$$

Three properties, each a one-line verification, are the content of the identification.

**It preserves the slice.** If $\tilde{X}^\dagger = -\tilde{X}$ then

$$
\left(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger\right)^\dagger
= \tilde{\Lambda}\tilde{X}^\dagger\tilde{\Lambda}^\dagger
= -\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger,
$$

so the image is again anti-Hermitian.

**It preserves the form.** By multiplicativity,

$$
N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger)
= N(\tilde{\Lambda})\,N(\tilde{X})\,N(\tilde{\Lambda}^\dagger)
= 1\cdot N(\tilde{X})\cdot\overline{N(\tilde{\Lambda})}
= N(\tilde{X}),
$$

using $N(\tilde{\Lambda}) = 1$ and $N(\tilde{\Lambda}^\dagger) = \overline{N(\tilde{\Lambda})} = 1$.

**It defines a homomorphism.** Since $\pi(\tilde{\Lambda}_1)\pi(\tilde{\Lambda}_2) = \pi(\tilde{\Lambda}_1\tilde{\Lambda}_2)$ and $(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger)^\dagger$ reuses the same $\tilde{\Lambda}$ on both sides, the assignment is a continuous group homomorphism

$$
\pi:\ SL(2,\mathbb{C}) = \{\tilde{\Lambda} : N(\tilde{\Lambda}) = 1\} \longrightarrow SO^+(1,3).
$$

Its kernel is the set of rotors acting trivially on every $\tilde{X}\in\mathbb{M}_-$. Since $-e_0$ is central,

$$
(-e_0)\,\tilde{X}\,(-e_0)^\dagger = \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger\big|_{\tilde{\Lambda} = -e_0}
= (-e_0)\tilde{X}(-e_0) = \tilde{X},
$$

so $\pm e_0$ act identically, and no other element does; hence

$$
\ker\pi = \{\pm e_0\}\cong\mathbb{Z}/2\mathbb{Z},
\qquad
SO^+(1,3)\cong SL(2,\mathbb{C})/\{\pm e_0\}.
$$

The map $\pi$ is **surjective** onto $SO^+(1,3)$; that every proper orthochronous Lorentz transformation of $\mathbb{M}_-$ arises as a rotor conjugation is the standard theorem that $SL(2,\mathbb{C})$ is the double cover of the restricted Lorentz group, and it is cited here as standard rather than re-derived. The identification of the previous section is therefore complete at the level of the identity component:

$$
\boxed{\; SO^+(1,3)\;\cong\;SL(2,\mathbb{C})/\{\pm e_0\}
\;=\;\{\pi(\tilde{\Lambda}): N(\tilde{\Lambda})=1\}/\ker\pi .\;}
$$

**Verification.** The two preservation properties and the kernel statement were checked numerically. Over three hundred random unit-norm rotors $\tilde{\Lambda} = R\,B$ (a rotation times a boost, normalized) applied to random anti-Hermitian $\tilde{X}$, the image was always anti-Hermitian and $|N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger) - N(\tilde{X})|$ was zero to machine precision. For a random rotor the identity $\pi(-\tilde{\Lambda}) = \pi(\tilde{\Lambda})$ held exactly.

A word on the relation between the complex and the real descriptions is in order, because the two groups have the same complexification. The complex group $SO(4,\mathbb{C})$ has complex dimension six; the real Lorentz group $SO(1,3)$ also has real dimension six, and is a real form of it. The rotor group $SL(2,\mathbb{C})$ is a six-real-dimensional group that doubly covers the identity component. The real structure is what reduces the first to the second; the map $\pi$ is what realizes the second by conjugation with unit-norm elements.

## The Infinitesimal Automorphisms: the Lie Algebra

Differentiating the unit-norm condition gives the Lie algebra of infinitesimal norm-form automorphisms. Let

$$
\tilde{\Lambda} = e_0 + \varepsilon\,\tilde{X},
\qquad \varepsilon\in\mathbb{R},\quad \varepsilon\ll1 .
$$

The condition $N(\tilde{\Lambda}) = 1$ becomes

$$
N(e_0+\varepsilon\tilde{X}) = (e_0+\varepsilon\tilde{X})(e_0+\varepsilon\bar{\tilde{X}})
= e_0 + \varepsilon\left(\tilde{X}+\bar{\tilde{X}}\right) + O(\varepsilon^2)
= e_0 + 2\varepsilon\,\mathrm{Sc}(\tilde{X}) + O(\varepsilon^2),
$$

so the tangent space at the identity is

$$
\mathfrak{sl}(2,\mathbb{C}) = \{\tilde{X}\in\mathbb{B} : \mathrm{Sc}(\tilde{X}) = 0\},
$$

the six-**real**-dimensional space spanned by the three real units and the three imaginary units,

$$
\mathfrak{sl}(2,\mathbb{C}) = \mathrm{span}_\mathbb{R}\{\,e_1,e_2,e_3,\ ie_1,ie_2,ie_3\,\}.
$$

This is the Lie algebra of the automorphism group, and it splits into **rotation** generators $\mathcal{J}_k = e_k$ (real quaternion directions) and **boost** generators $\mathcal{K}_k = ie_k$ (imaginary vector directions). Their brackets are computed directly from the quaternion multiplication rule; the commutator is $[A,B] = AB-BA$, and

$$
[\mathcal{J}_j,\mathcal{J}_k] = 2\varepsilon_{jkl}\mathcal{J}_l,
\qquad
[\mathcal{J}_j,\mathcal{K}_k] = 2\varepsilon_{jkl}\mathcal{K}_l,
\qquad
[\mathcal{K}_j,\mathcal{K}_k] = -2\varepsilon_{jkl}\mathcal{J}_l .
$$

The first two say that the rotations close and that the boosts transform as a vector under them; the third, with its minus sign, is the algebraic statement that two boosts do not close into a boost but into a rotation plus a boost. This is the infinitesimal form of the Thomas–Wigner rotation, and the sign is the one that makes the boost directions a vector and the rotation directions an axial vector.

**Verification.** The three bracket families above were checked exactly, as identities in the quaternion algebra, for all $j,k\in\{1,2,3\}$: they reproduce the standard Lorentz algebra $\mathfrak{so}(1,3)$ up to the conventional factor two. For example $[\mathcal{J}_1,\mathcal{J}_2] = 2e_3$ and $[\mathcal{K}_1,\mathcal{K}_2] = -2e_3$, both confirmed.

**The complexification and the two factors.** Complexifying the real Lie algebra and forming

$$
\mathcal{N}^{\pm}_k = \tfrac14\left(\mathcal{J}_k \pm \mathrm{i}\,\mathcal{K}_k\right),
$$

where $\mathrm{i}$ is the complexification unit — distinct from the algebra's own central $i$ — gives two commuting copies of the rotation algebra,

$$
[\mathcal{N}^{+}_j,\mathcal{N}^{+}_k] = \varepsilon_{jkl}\mathcal{N}^{+}_l,
\qquad
[\mathcal{N}^{-}_j,\mathcal{N}^{-}_k] = \varepsilon_{jkl}\mathcal{N}^{-}_l,
\qquad
[\mathcal{N}^{+}_j,\mathcal{N}^{-}_k] = 0 .
$$

The factor $\tfrac14$ is forced by the normalization $[\mathcal{J}_j,\mathcal{J}_k] = 2\varepsilon_{jkl}\mathcal{J}_l$. With $\mathcal{K}_k = ie_k$ and $\mathrm{i}$ a second central imaginary unit, the combination can be written $\mathcal{N}^{\pm}_k = \tfrac14\left(1 \pm \mathrm{i} i\right)e_k$, and its central factor is idempotent up to a factor two,

$$
\left(1 \pm \mathrm{i} i\right)^2 = 2\left(1 \pm \mathrm{i} i\right),
\qquad\text{because}\qquad
(\mathrm{i} i)^2 = \mathrm{i}^2 i^2 = +e_0 .
$$

This is what makes each combination close on itself with the same structure constants, and what makes the two commute: $\left(1 + \mathrm{i} i\right)\left(1 - \mathrm{i} i\right) = 1 - (\mathrm{i} i)^2 = 0$. For $[\mathcal{N}^{+}_j,\mathcal{N}^{+}_k]$ the central factor contributes $(1+\mathrm{i} i)^2 = 2(1+\mathrm{i} i)$ and the quaternion commutator contributes $[e_j,e_k] = 2\varepsilon_{jkl}e_l$, so the product is $4\varepsilon_{jkl}\left(1+\mathrm{i} i\right)e_l/16 = \varepsilon_{jkl}\mathcal{N}^{+}_l$, as displayed. The combinations are the ones that diagonalize the adjoint action of the complexified boost generator. This is the Lie-algebra shadow of the group isomorphism $SO(4,\mathbb{C})\cong(SL(2,\mathbb{C})\times SL(2,\mathbb{C}))/\mathbb{Z}_2$ of the complex section: the two factors are the two commuting $\mathfrak{su}(2)$ algebras. The care needed here is that $\mathrm{i}$ is the complexification unit and not the algebra's scalar imaginary; the latter already appears in $\mathcal{K}_k = ie_k$, and conflating the two would be a notational error. The distinction is the same one that separates the real form $\mathfrak{so}(1,3)$ from its complexification.

## What the Algebra Supplies and What Is Standard

**Supplied by the algebra.** The fact that the norm form is multiplicative, and therefore that it is the algebra's own quadratic structure; the determinant realization $N = \det$, which turns the automorphism problem into a problem about $M_2(\mathbb{C})$; the restriction of the complex form to the real slices, with the signature table; the identification of the automorphisms preserving the material slice with $O(1,3)$, and of the identity component with the rotor conjugations; and the infinitesimal algebra with its rotation-boost split and its minus sign on the boost-boost bracket.

**Standard mathematics transcribed.** The classification of nondegenerate complex quadratic forms, the isomorphism $SO(4,\mathbb{C})\cong(SL(2,\mathbb{C})\times SL(2,\mathbb{C}))/\mathbb{Z}_2$, the double cover $SL(2,\mathbb{C})\to SO^+(1,3)$, and the real forms of $\mathfrak{so}(4,\mathbb{C})$ are standard Lie theory. The surjectivity of the rotor map is the standard covering theorem and is cited, not re-derived; what is derived here is the algebraic form of the action and its kernel.

**Interpretation.** The reading of the material slice as physical spacetime, and of its norm-form automorphisms as the Lorentz group, is the framework's structural hypothesis. The group-theoretic content is exact; the physical assignment is the hypothesis, and it is the same hypothesis that the foundational articles *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* and *Introduction to the Biquaternion Universe* state.

## Open Questions

1. **Automorphisms of the full algebra.** The maps considered here preserve the norm form and, at the real level, the material slice. The $\mathbb{C}$-algebra automorphisms of $\mathbb{B}\cong M_2(\mathbb{C})$ are the inner automorphisms, $X\mapsto\tilde{A}X\tilde{A}^{-1}$, a subgroup of the form automorphisms. Does the framework assign a physical role to the difference between algebra automorphisms and form automorphisms?

2. **The discrete components.** $O(1,3)$ has four components; the rotor group covers only $SO^+(1,3)$. Parity and time reversal are form automorphisms outside the rotor group. Whether the framework can represent them by an operation on biquaternion fields — rather than on four-vectors — without leaving the algebra is not settled here.

3. **Real forms and the two sectors.** Both $\mathbb{M}_-$ and $\mathbb{M}_+$ restrict the form to a Lorentzian signature — $(3,1)$ on the material slice and $(1,3)$ on the informational one — and $\mathbb{H}_{\mathbb{B}}$ to $(4,0)$. The Euclidean real form is thus available. Is the Euclidean form, and the compact group it defines, the home of the informational sector's own symmetries? The question connects this article to *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*.

4. **The norm form and curved spacetime.** The automorphism characterization is pointwise and flat. Whether it globalizes to a bundle of algebra automorphisms over a curved base, and what plays the role of the form there, is the same open question the foundational articles record for the whole framework.

5. **Uniqueness of the physical group.** The form determines $O(4,\mathbb{C})$ uniquely; the real structure then determines its real forms. Could a different real structure on $\mathbb{B}$ select a different physical group, and does the algebra rule out such a choice?

The conventions of the construction are those of the following companion articles:

- Companion article *Introduction to the Biquaternion Universe*, for the notation, the norm form and the sector structure.
- Companion article *Conventions in the Biquaternion Universe*, for the algebra and basis, the conjugations, the real subspaces and the metric at its three levels.
- Companion article *The Lorentz Group in Biquaternionic Form — Structure and Representations*, for the Lie algebra, the real forms and the representation theory.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the defining module and the action of the group on it.
- Companion article *The Light Cone as the Biquaternion Zero-Divisor Cone*, for the cone preserved by the automorphisms.
- Companion article *The Two-Sheeted Cover and the Topology of Boosts in Biquaternionic Form*, for the covering group and the global structure.

## Summary

The norm form $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ is a nondegenerate multiplicative quadratic form on $\mathbb{B}\cong\mathbb{C}^4$, with polarization matrix the identity and with

$$
N(\tilde{Q}\tilde{R}) = N(\tilde{Q})N(\tilde{R}),
\qquad
N(\tilde{Q}^\dagger) = \overline{N(\tilde{Q})}.
$$

Its automorphism group at the complex level is $O(4,\mathbb{C})$, whose connected component is

$$
SO(4,\mathbb{C}) \cong \frac{SL(2,\mathbb{C})\times SL(2,\mathbb{C})}{\{\pm(e_0,e_0)\}},
$$

realized by $\tilde{X}\mapsto\tilde{A}\tilde{X}\tilde{B}^{-1}$ with $\det\tilde{A}=\det\tilde{B}=1$. The algebra's real structure selects the anti-Hermitian slice $\mathbb{M}_-$, on which the form restricts to

$$
N(ict\,e_0+\mathbf{x}) = -c^2t^2+\mathbf{x}^2,
\qquad
\eta = \mathrm{diag}(-1,+1,+1,+1),
$$

so the automorphisms preserving the slice form $O(1,3)$, with identity component the restricted Lorentz group. That component is exactly the group of rotor conjugations,

$$
SO^+(1,3)\cong SL(2,\mathbb{C})/\{\pm e_0\},
\qquad
\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger,
\qquad
N(\tilde{\Lambda})=1,
$$

the map being two-to-one with kernel $\{\pm e_0\}$. Infinitesimally, the algebra is $\mathfrak{sl}(2,\mathbb{C}) = \{X : \mathrm{Sc}(X)=0\}$, spanned by the rotation generators $\mathcal{J}_k = e_k$ and the boost generators $\mathcal{K}_k = ie_k$, with

$$
[\mathcal{J}_j,\mathcal{J}_k] = 2\varepsilon_{jkl}\mathcal{J}_l,
\qquad
[\mathcal{J}_j,\mathcal{K}_k] = 2\varepsilon_{jkl}\mathcal{K}_l,
\qquad
[\mathcal{K}_j,\mathcal{K}_k] = -2\varepsilon_{jkl}\mathcal{J}_l,
$$

whose complexification splits into two commuting rotation algebras. The Lorentz group, in this reading, is what the norm form's automorphisms become when they are required to respect the algebra's real structure.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$; $i$ | Quaternion basis ($e_k^2=-e_0$); central scalar imaginary |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form; level-1 identity on $\mathbb{C}$ |
| $B(\tilde{Q},\tilde{R}) = \sum_\mu Q_\mu R_\mu$ | Polar (symmetric bilinear) form, matrix $G=I_4$ |
| $O(4,\mathbb{C}),\ SO(4,\mathbb{C})$ | Complex automorphism group of $N$; its identity component |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$, $\Phi(e_k)=-i\sigma_k$, $N=\det\Phi$ | Matrix realization; norm form is the determinant |
| $T_{\tilde{A},\tilde{B}}:\tilde{X}\mapsto\tilde{A}\tilde{X}\tilde{B}^{-1}$ | General norm-preserving complex map |
| $SO(4,\mathbb{C})\cong(SL(2,\mathbb{C})\times SL(2,\mathbb{C}))/\{\pm(e_0,e_0)\}$ | Complex group |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) slices |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{C}_{\mathbb{B}}$ | Real-quaternion, imaginary-quaternion, complex scalar subalgebras |
| $\eta=\mathrm{diag}(-1,+1,+1,+1)$ | Level-2 Minkowski form, restriction of $N$ to $\mathbb{M}_-$ |
| $O(1,3)$, $SO^+(1,3)$ | Lorentz group; restricted (proper orthochronous) Lorentz group |
| $\tilde{\Lambda}$, $N(\tilde{\Lambda})=1$ | Unit-norm biquaternion (Lorentz rotor) |
| $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation; the automorphism of the slice |
| $\pi:SL(2,\mathbb{C})\to SO^+(1,3)$, $\ker\pi=\{\pm e_0\}$ | Two-to-one covering homomorphism |
| $\mathfrak{sl}(2,\mathbb{C}) = \{X:\mathrm{Sc}(X)=0\}$ | Lie algebra; $\mathcal{J}_k=e_k$ (rotations), $\mathcal{K}_k=ie_k$ (boosts) |
| $[\mathcal{K}_j,\mathcal{K}_k]=-2\varepsilon_{jkl}\mathcal{J}_l$ | Boosts do not close; infinitesimal Wigner rotation |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- Hermann Weyl, *The Classical Groups: Their Invariants and Representations* (Princeton, 1946), for the orthogonal groups and the isomorphisms of low-dimensional classical groups.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for real forms of complex Lie algebras and the classification of the Lorentz group's real forms.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the covering groups, the exponential map and the isomorphism $SO(4,\mathbb{C})\cong(SL_2\times SL_2)/\mathbb{Z}_2$.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the identification of $SL(2,\mathbb{C})$ with the spin group and the double cover of the Lorentz group.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component realization of the restricted Lorentz group and its Lie algebra.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor representation of the Lorentz group and the boost–rotation decomposition.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the even-subalgebra and bivector formulation of the Lorentz group.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Lorentz group, its complexification and its finite-dimensional representations.
