# __Why the Multipole Tower Is Infinite but the Biquaternion Algebra Is Not__

## Introduction

The two preceding articles expand the field of a localised source in an infinite series of multipole moments, and follow the same series through the vibrating and rotating ellipsoid. The tower is genuinely infinite: a generic source has moments $q_{lm}$ for every order $l = 0, 1, 2, \dots$, each order carrying $2l+1$ independent components, and a generic vibrating body has a normal mode for every $l$ as well. The biquaternion algebra, by contrast, is finite-dimensional: four complex dimensions, eight real dimensions, spanned by the basis $e_0, e_1, e_2, e_3$. The question this article addresses is how a finite algebra can host an infinite tower.

The question is worth taking seriously, because it is easy to ask it in a form that has no answer. If one expects the multipole moments to be *elements a field can take* — values of the algebra at each point — then an infinite tower cannot sit inside a four-dimensional algebra, and one might look for a larger algebra, or suspect an inconsistency. The resolution is that the tower is not a tower of algebra elements at all. The multipole order $l$ is a label of the angular structure of a **function** on the sphere; the tower is the decomposition of the infinite-dimensional function space into irreducible representations of the rotation group. The biquaternion algebra is the **value space** — the algebra in which the field takes its values at a point — and it is finite because it is the value algebra of a two-state, four-vector structure. Two different mathematical objects, of two different dimensions, are doing two different jobs, and there is no contradiction between them.

There is also a sharper statement to make, and it is the strongest form of the answer. As a representation space of the rotation group, the biquaternion algebra decomposes as $D^{(0)}\oplus D^{(1)}$ — the trivial representation and the vector representation — and contains no representation of order $l\geq2$. Its **elements** therefore carry the monopole and the dipole and nothing higher, and its **product** cannot manufacture anything higher either, because the quaternion product of two vectors, $\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v}$, keeps only the dot and the cross product and discards precisely the symmetric traceless part that a quadrupole would be. Not only does the algebra not *contain* the tower; it cannot *reach* it by multiplication. The tower lives elsewhere, in the function space and in the infinite-dimensional enveloping algebra of the rotation generators.

The article is structural and classical, and it stays inside the non-relativistic series; the algebra it examines is the same finite algebra used throughout. Conventions are those of the companion articles:
- Companion article *Introduction to the Biquaternion Universe*, for the algebra and its two sectors.
- Companion article *Conventions in the Biquaternion Universe*, for the trace, the metric at its three levels, and the conventions of presentation.
- Companion article *Biquaternion Representation Theory*, for the algebra as a complex algebra and its modules.
- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the rotation generators and the spin operators inside the algebra.
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the trace obstruction that is the companion phenomenon in the bracket setting.
- Companion article *The Multipole Expansion and the Quadrupole Interaction in Biquaternionic Form*, for the multipole series and the quadrupole as a symmetric traceless tensor.
- Companion article *The Vibrating Ellipsoid and Higher-Multipole Oscillations in Biquaternionic Form*, for the oscillating tower of a deformed body.

The algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and central scalar imaginary $i$, $i^2 = -1$; the vector part is $\mathbf{v} = v_1e_1 + v_2e_2 + v_3e_3$; the material sector is $\mathbb{M}_-$ and the informational sector $\mathbb{M}_+$; the rotation generators are built from $e_1, e_2, e_3$; and $D^{(l)}$ denotes the irreducible complex representation of the rotation group of dimension $2l+1$, in the convention in which the monopole is $D^{(0)}$, the dipole and every spatial vector is $D^{(1)}$, and the quadrupole is $D^{(2)}$.

## The Two Facts

### The Algebra Is Finite-Dimensional

Every element of $\mathbb{B}$ is a unique complex linear combination of the four basis elements,

$$
\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3 ,
\qquad Q_0, Q_1, Q_2, Q_3 \in \mathbb{C} ,
$$

so $\dim_{\mathbb{C}}\mathbb{B} = 4$ and $\dim_{\mathbb{R}}\mathbb{B} = 8$. The algebra closes on itself: the product of two basis elements is again a basis element up to signs, and the product of two general elements is again a four-component object. Equivalently, with $e_k\mapsto -i\sigma_k$ and $e_0\mapsto I_2$, the algebra is the matrix algebra

$$
\mathbb{B} \cong M_2(\mathbb{C}) ,
$$

whose dimension is four. Every algebraic fact below is a fact about a four-dimensional complex algebra.

The finiteness is not an accident of the basis. An algebra that contains the unit and is generated by three elements $e_1, e_2, e_3$ with the quaternion relations is four-dimensional because those relations exhaust the algebra: any word in the generators reduces, using $e_ie_j = -\delta_{ij}e_0 + \epsilon_{ijk}e_k$, to a linear combination of $e_0, e_1, e_2, e_3$. There is no room for a fifth independent element.

### The Tower Is Infinite

The multipole moment of order $l$ is an element of the irreducible representation $D^{(l)}$ of the rotation group, of complex dimension $2l+1$. The orders run over all $l = 0, 1, 2, \dots$ without bound, and the field's angular dependence is the direct sum

$$
L^2(S^2) = \bigoplus_{l=0}^{\infty} D^{(l)} ,
$$

in which each $D^{(l)}$ appears exactly once; the spherical harmonic $Y_l^m$ belongs to $D^{(l)}$. The expansion coefficients — the multipole moments — are the components of the field in this decomposition, and a generic source populates every $l$. The same tower appears in the vibrating body of the second article, one normal mode per order, with $2l+1$ amplitudes $a_{lm}$ at order $l$. In both cases the tower is infinite because the space of angular functions is infinite-dimensional.

### Counting the Capacity

A finite-dimensional complex vector space on which the rotation group acts decomposes into finitely many irreducibles, and the dimension is the sum of their dimensions,

$$
d = \sum_{i} n_i\,(2l_i+1) ,
$$

where $n_i$ is the multiplicity of $D^{(l_i)}$. For the biquaternion algebra $d = 4$, the only ways to write $4$ as a sum of numbers of the form $2l+1 = 1, 3, 5, \dots$ are

$$
4 = 1 + 1 + 1 + 1 \quad\text{and}\quad 4 = 1 + 3 ,
$$

so a four-dimensional rotation module can be four copies of $D^{(0)}$, or one copy each of $D^{(0)}$ and $D^{(1)}$. Nothing else. In particular $l = 2$ would require at least a $D^{(2)}$, of dimension $5$, which already exceeds the total dimension, and every higher $l$ exceeds it further. **No four-dimensional space can contain a quadrupole as an irreducible subspace.** The largest multipole order an element of $\mathbb{B}$ can carry is $l = 1$.

## Three Representation-Theoretic Roles of the Algebra

Before the decomposition can be read correctly, it is necessary to separate three distinct roles that the algebra plays, because conflating them is the usual source of confusion.

### As a Rotation Module: $\mathbb{B} = D^{(0)}\oplus D^{(1)}$

The rotation group acts on $\mathbb{B}$ by rotor conjugation, $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\bar{\tilde{\Lambda}}$ with $\tilde{\Lambda}\in\mathbb{H}_{\mathbb{B}}$ a real unit quaternion. Under this action the center $\mathbb{C}_{\mathbb{B}} = \{Q_0e_0\}$ is pointwise fixed and the traceless part $\mathfrak{sl}_2(\mathbb{C}) = \{Q_1e_1+Q_2e_2+Q_3e_3\}$ transforms as a vector:

$$
\mathbb{B} = D^{(0)}\oplus D^{(1)} \qquad\text{(as a complex rotation module)},
\qquad 1 + 3 = 4 .
$$

The weight spectrum confirms it, and it also shows why only integral $l$ can occur. The action is rotor conjugation, and $-\tilde{\Lambda}$ gives the same conjugation as $\tilde{\Lambda}$, so this action factors through the rotation group $SO(3)$ and cannot see the double cover: every irreducible representation it can contain has integral angular momentum. (The half-integral representations are not excluded from the algebra, but they cannot appear from this action; they appear from the *left multiplication* discussed in the next subsection.) For a rotation about a fixed axis, the center is fixed, the axis element is fixed, and the two combinations transverse to the axis are eigenvectors with phases $e^{\mp i\theta}$; the weights are $0$, $0$, $+1$, $-1$, and there is no weight $\pm2$ state that a $D^{(2)}$ would require. Equivalently, the character of the conjugation action equals

$$
2 + 2\cos\theta = \chi_0(\theta) + \chi_1(\theta),
$$

the sum of the spin-$0$ and spin-$1$ characters, with the spin-$2$ character $\chi_2 = 1+2\cos\theta+2\cos2\theta$ absent. This is the role in which the algebra is the **value space** of the multipole problem, and the role in which it is capped at $l = 1$.

### As an Algebra: Simple, with the Spinor Module

The same four-dimensional object is also an algebra, and as an algebra it is simple: $M_2(\mathbb{C})$ has no nontrivial two-sided ideals, and up to isomorphism it has a single irreducible left module, the two-dimensional spinor space $S$, a minimal left ideal,

$$
S = \mathbb{B}\,\epsilon , \qquad \epsilon^2 = \epsilon \neq 0 , \qquad \dim_{\mathbb{C}} S = 2 ,
$$

on which the rotation generators act by left multiplication as the spin-$\tfrac12$ representation. The spin-$\tfrac12$ content belongs to the **module**, not to the algebra-as-rotation-module of the previous subsection. The two facts — the algebra is $D^{(0)}\oplus D^{(1)}$ under conjugation, and its irreducible module is spin-$\tfrac12$ — are both true and are not in tension, because they are statements about different actions.

### As a Product: $D^{(1)}\times D^{(1)}\to D^{(0)}\oplus D^{(1)}$

The third role is the multiplication map. The tensor product of two vector representations decomposes by the Clebsch–Gordan series as

$$
D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)} ,
\qquad 3\times 3 = 1 + 3 + 5 ,
$$

and the algebra's product is the part of this tensor product that lands back in $\mathbb{B}$,

$$
D^{(1)}\times D^{(1)} \longrightarrow D^{(0)}\oplus D^{(1)} \subset \mathbb{B} ,
\qquad
\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v} .
$$

The dot product is the $D^{(0)}$ channel and the cross product is the $D^{(1)}$ channel; the symmetric traceless $D^{(2)}$ channel is not in the image. This is the role that closes the argument: the algebra does not merely fail to contain a quadrupole, its product cannot create one from vectors.

The three roles can be summarised in one line each: the algebra *as a value space* is $D^{(0)}\oplus D^{(1)}$; the algebra *as an algebra* acts on the spin-$\tfrac12$ module; the algebra *as a product* truncates $D^{(1)}\otimes D^{(1)}$ to $D^{(0)}\oplus D^{(1)}$. Only the first and the third constrain the multipole content, and both stop at $l = 1$.

## The Truncating Product and the Truncating Gradient

### The Product

From the three roles above, the product of two elements of $\mathbb{B}$ stays in $\mathbb{B}$ — that is what it means to be an algebra — and, restricted to the traceless part, it maps $D^{(1)}\otimes D^{(1)}$ onto $D^{(0)}\oplus D^{(1)}$. The truncation is visible in the symmetrization identities for pure vectors $\mathbf{u}, \mathbf{v}$:

$$
\tfrac12\left(\mathbf{u}\mathbf{v} + \mathbf{v}\mathbf{u}\right) = -(\mathbf{u}\cdot\mathbf{v})\,e_0 \in D^{(0)} ,
\qquad
\tfrac12\left(\mathbf{u}\mathbf{v} - \mathbf{v}\mathbf{u}\right) = \mathbf{u}\times\mathbf{v} \in D^{(1)} .
$$

The symmetric traceless part of $\mathbf{u}\otimes\mathbf{v}$, the $D^{(2)}$ channel, is annihilated by the symmetrized product. In angular-momentum language this is the statement that the symmetrized product of two vectors contains only the $l = 0$ and $l = 1$ combinations, and never the $l = 2$ one. Both identities were verified on random vector pairs.

### The Gradient

The same truncation appears at the level of derivatives, and it is the form in which the multipole expansion actually meets the algebra. The spatial vector gradient is $\boldsymbol{\nabla} = e_1\partial_x + e_2\partial_y + e_3\partial_z$, and its square is

$$
\boldsymbol{\nabla}\,\boldsymbol{\nabla} = \sum_{i,j}e_ie_j\,\partial_i\partial_j = -\Delta\,e_0 ,
$$

because the antisymmetric part of the product multiplies the symmetric operator $\partial_i\partial_j$ and cancels, leaving only the trace. The second gradient of any scalar potential is therefore a **purely central** element: whatever traceless symmetric structure $\partial_i\partial_j\Phi$ has, the product of two gradient operators discards it. This was verified on a quadratic potential with a random symmetric Hessian, for which $\sum_{ij}e_ie_j\,H_{ij} = -\mathrm{tr}(H)e_0$ exactly. The derivative operator, like the algebra, stops at the trace.

The two facts together — the algebra's product and its gradient — say that the finite object can iterate a vector operation arbitrarily many times and still produce only $D^{(0)}\oplus D^{(1)}$ content. The multipole order cannot be raised by multiplication or by differentiation inside the algebra.

## Where the Tower Actually Lives

The tower is real, so it must live somewhere. There are five equivalent descriptions of its home, and all of them are infinite-dimensional.

**(i) The function space.** The multipole moments are the coefficients of a function on the sphere in the spherical harmonics, $L^2(S^2) = \bigoplus_l D^{(l)}$. The field of a localised source is a function of position, so its angular dependence lives in an infinite-dimensional function space. The values of that function are in $\mathbb{B}$; the angular structure is in the function space. This is the description used in the first two articles.

**(ii) The symmetric traceless tensor powers.** The order-$l$ moment is a symmetric traceless rank-$l$ tensor over the vector part,

$$
\operatorname{Sym}^l_0(D^{(1)}) \cong D^{(l)} ,
\qquad
\dim_{\mathbb{C}}\operatorname{Sym}^l_0(D^{(1)}) = 2l+1 ,
$$

which for $l = 2$ is the $\operatorname{Sym}^2_0(D^{(1)})\cong D^{(2)}$ of the quadrupole. The tower is the collection of all these tensor powers, and the space they span is infinite-dimensional. The algebra $\mathbb{B}$ is the $l\leq1$ part of this collection; the higher powers live outside it.

**(iii) The universal enveloping algebra.** The rotation generators $J_1, J_2, J_3$ (equivalently, the algebra elements $e_k$ with their commutators) generate the universal enveloping algebra $U(\mathfrak{su}(2))$, whose elements are the polynomials in the generators. By the Poincaré–Birkhoff–Witt theorem it has a basis of ordered monomials and is **infinite-dimensional**, and it carries every irreducible representation $D^{(l)}$, because each $D^{(l)}$ is generated from a highest-weight vector by repeated application of the lowering generator. The enveloping algebra is an algebra — not merely a function space — that does contain the whole tower as its finite-dimensional modules, and it is exactly the enlargement the multipole series calls for. It is infinite-dimensional, and it must be.

**(iv) The differential-operator algebra.** The operators generated by $\boldsymbol{\nabla}$ and the coordinate multiplications, acting on functions, form an infinite-dimensional algebra; the multipole moments are linear functionals on it, obtained by integrating the source against spherical harmonics. The moments are not values of the field but integrals over the source,

$$
q_{lm} = \int \rho(\mathbf{x}')\,r'^{\,l}\,Y_l^{m*}(\theta',\phi')\,d^3x' ,
$$

and a functional of the source is not an element of the value algebra. This is the most direct reason the tower does not need to fit inside $\mathbb{B}$.

**(v) The harmonic polynomials.** The order-$l$ content of the source is also carried by the *solid harmonics* $r^lY_l^m$, which are exactly the harmonic polynomials of degree $l$ in the coordinates: $2l+1$ of them at each degree. Every polynomial in $x, y, z$ decomposes into harmonic polynomials of various degrees, the harmonic part of degree $l$ is the $D^{(l)}$, and the order-$l$ moment is the coefficient of the corresponding solid harmonic in the expansion of the source. The polynomial algebra is graded by degree and infinite-dimensional. The algebra $\mathbb{B}$ is four-dimensional: it has room for a constant and a vector — the degree-$0$ and degree-$1$ data — and none for a harmonic polynomial of degree $l \geq 2$.

These five descriptions are the same statement in five languages. The tower is a property of a graded, infinite-dimensional structure — functions, tensor powers, polynomials in the generators, harmonic polynomials, or differential operators — and the biquaternion algebra is the degree-$\leq1$ truncation of that structure.

## Two Infinities, One Field

It is worth separating two infinities that meet in this problem, because they are distinct and only one of them is the tower.

The first is the **spatial continuum**. A classical field is a value at each point of a continuous space, so the space of field configurations is infinite-dimensional even before any angular decomposition: it is a space of functions on $\mathbb{R}^3$. The second is the **angular tower**. The decomposition of a function on the sphere into spherical harmonics is infinite, because the sphere has infinitely many irreducible angular modes. The multipole tower is this second infinity, the angular one.

The biquaternion algebra is a finite answer to a different question: what is the value at a single point? A point carries a biquaternion, four complex numbers, and that is finite. The map from the continuum of points to the finite algebra has both infinities — the continuum of the domain and the angular tower of the spherical harmonics — and neither of them requires the algebra to be infinite. The algebra is the codomain, not the domain and not the decomposition.

## The No-Go Statement

The observations of the previous sections combine into a general statement.

**Proposition.** No finite-dimensional complex algebra on which the rotation group acts by algebra automorphisms can contain the irreducible representations $D^{(l)}$ for all $l\geq0$ as subquotients of its rotation module.

**Proof.** Let $A$ be such an algebra. It is a finite-dimensional complex $SU(2)$-module, so it has a Jordan–Hölder composition series with finitely many simple factors, and each simple factor is isomorphic to some $D^{(l)}$ because the finite-dimensional simple $SU(2)$-modules are exactly the $D^{(l)}$. A finite series has finitely many factors, so only finitely many distinct values of $l$ can occur among the subquotients. But the set $\{D^{(l)}\}_{l\geq0}$ is infinite and its members are pairwise non-isomorphic, so not all of them can occur. $\square$

**Corollary.** The biquaternion algebra, of complex dimension four, has rotation content $D^{(0)}\oplus D^{(1)}$, and it contains $D^{(l)}$ for $l\geq2$ in no subspace and in no composition factor. Its elements carry the monopole and the dipole, and nothing higher.

One nuance prevents the proposition from being read too broadly. The finiteness of an algebra does **not** by itself forbid it from having infinite-dimensional representations: $M_2(\mathbb{C})$, though four-dimensional, has infinite-dimensional modules (the algebra acting on a space of functions, for instance). What the counting argument forbids is the tower sitting *inside* the algebra as a rotation submodule or subquotient — which is exactly what the assertion "the quadrupole is an algebra element" would require. The field is an infinite-dimensional module of the algebra without difficulty; the moments are not elements of the algebra. The two statements are different, and only the second is obstructed.

The proposition also rules out the natural hope of repairing the situation by enlarging the algebra a little. Enlarging is possible, and it does buy higher orders, but always finitely many. The smallest matrix algebra whose rotation module contains a $D^{(2)}$ is $M_3(\mathbb{C})$, of complex dimension nine, with the rotation group embedded so that its fundamental three-dimensional representation restricts to $D^{(1)}$; then

$$
M_3(\mathbb{C}) = D^{(0)}\oplus D^{(1)}\oplus D^{(2)} ,
\qquad 1 + 3 + 5 = 9 ,
$$

which does contain the quadrupole. The price is the loss of the two-dimensional spinor module that makes $\mathbb{B}$ a qubit-like algebra: $M_3(\mathbb{C})$ has a three-dimensional irreducible module, and its rotational content, while larger, is no longer the two-state structure of the biquaternion framework. Going further still, the tensor square $\mathbb{B}\otimes\mathbb{B}$, of complex dimension sixteen, contains

$$
(D^{(0)}\oplus D^{(1)})\otimes(D^{(0)}\oplus D^{(1)}) = 2D^{(0)}\oplus 3D^{(1)}\oplus D^{(2)} ,
\qquad 2 + 9 + 5 = 16 ,
$$

whose $D^{(2)}$ summand is again present — but $D^{(3)}$ and above are still missing. No finite enlargement ever catches the tower, by the proposition. The tower is intrinsically infinite-dimensional, and its natural algebraic carrier is the infinite-dimensional enveloping algebra $U(\mathfrak{su}(2))$; no finite-dimensional algebra carries it.

## Why Both Infinities and Finitenesses Are Necessary

It is worth saying why the contrast is not a defect to be repaired but a structural necessity.

The algebra is finite because it is the **local value space** of the theory. A point of spacetime carries a finite amount of algebraic data — here four complex numbers — and the whole purpose of a finite algebra of values is to be finite. Its four dimensions carry the two-dimensional spinor module, which is what makes it qubit-like, and, under rotations, the scalar-plus-vector content $D^{(0)}\oplus D^{(1)}$, which is what makes it a four-vector; those two readings are the algebra's physical role.

The tower is infinite because the theory is a **field theory**. A classical field on three-dimensional space has infinitely many angular degrees of freedom; there is no largest multipole order, and a generic source excites all of them. The infinity is the infinity of the function space, and it is the same infinity that makes a field a field rather than a finite set of numbers.

The two statements are therefore not in competition. The field is a map from an infinite set of points to the finite algebra; at each point the value is a biquaternion, and across the continuum of points the angular structure is infinite. The multipole tower is the angular decomposition of the map, not of the value. When the first two articles say that the quadrupole is not an algebra element, this is the precise sense of the statement: the quadrupole is a feature of the map, and the algebra is the algebra of the values.

## The Capacity of the Algebra and Its Enlargements

The representation content of an algebra, under a chosen rotation action, can be tabulated, and the table makes the trade-off concrete. The representative cases are the biquaternion algebra, its tensor square, the smallest matrix algebra that reaches the quadrupole, and the enveloping algebra.

| Algebra | $\dim_{\mathbb{C}}$ | Rotation content | Highest multipole | Irreducible module |
|---|---|---|---|---|
| $\mathbb{B} \cong M_2(\mathbb{C})$ | $4$ | $D^{(0)}\oplus D^{(1)}$ | $l = 1$ | dimension $2$ (spin $\tfrac12$) |
| $M_3(\mathbb{C})$ | $9$ | $D^{(0)}\oplus D^{(1)}\oplus D^{(2)}$ | $l = 2$ | dimension $3$ (spin $1$) |
| $\mathbb{B}\otimes\mathbb{B} \cong M_4(\mathbb{C})$ | $16$ | $2D^{(0)}\oplus 3D^{(1)}\oplus D^{(2)}$ | $l = 2$ | dimension $4$ |
| $U(\mathfrak{su}(2))$ | infinite | all $D^{(l)}$, each with infinite multiplicity | unbounded | the $D^{(l)}$ themselves are finite-dimensional; the Verma modules are infinite-dimensional and reducible |

Reading down the table, the pattern is clear. Every enlargement buys a finite amount of new representation content, and the price is paid in the module structure: $M_2(\mathbb{C})$ has the two-dimensional module that makes it qubit-like, $M_3(\mathbb{C})$ has a three-dimensional module, $M_4(\mathbb{C})$ a four-dimensional one. Only the infinite-dimensional enveloping algebra reaches every $l$, and it does so by being infinite-dimensional in the first place. The biquaternion algebra occupies the first row, and the multipole series of the first two articles uses exactly its content — monopole and dipole as elements, quadrupole and above as tensors.

A clarification of vocabulary is worth making here. The intrinsic spin content of the algebra — what it can hold as a *local* representation — is spin $0$ and spin $1$ as values, together with the spin-$\tfrac12$ irreducible module. The multipole order of the tower is **orbital** angular structure of the field, not intrinsic spin, and there is no reason for the two to be bounded by one another. The algebra bounds the intrinsic spin; the field's angular decomposition is bounded by nothing.

## The Same Finite-Dimensionality Elsewhere

The obstruction met here is not isolated; it is one instance of a general feature of finite-dimensional algebras, and the companion articles record others.

Inside $\mathbb{B}$ the canonical commutation relation of quantum mechanics, $[\tilde{Q}, \tilde{P}] = i\hbar\,e_0$, cannot be realized: taking the trace of both sides gives $0 = \mathrm{Tr}(i\hbar\,e_0) = 2i\hbar \neq 0$, a contradiction, because the trace of a commutator vanishes. This is the trace obstruction, and it is the statement that the Heisenberg algebra has no finite-dimensional representation. The multipole obstruction is the same phenomenon in a different disguise:
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the trace obstruction and the canonical bracket.

Likewise the rotation generators themselves close inside the algebra — the spin operators are algebra elements — but the *eigenstates* of those operators, the tower of angular momentum states $|l,m\rangle$, do not fit inside the algebra; they live in the modules $D^{(l)}$, of dimensions $2l+1$ growing without bound:
- Companion article *Angular Momentum and Spin in Biquaternionic Form*, for the spin operators as algebra elements and the representation content.

The comparison with a finite group makes the counting vivid. The group algebra of a **finite** group is finite-dimensional, has finitely many irreducible representations, and its regular representation is a finite direct sum of them; nothing of the representation theory is left over. The biquaternion algebra behaves in this respect like such a finite group algebra: four-dimensional, two irreducible summands, no leftover. The rotation group $SU(2)$ is compact but infinite, and its group algebra (in the $L^2$ sense) decomposes by the Peter–Weyl theorem as $\bigoplus_l \overline{D^{(l)}}\otimes D^{(l)}$, carrying every $D^{(l)}$ and infinite-dimensional. The multipole tower is the content of that continuous regular representation, and the biquaternion algebra is a finite truncation of it.

In every case the pattern is the same: the *generators* and the *values* are finite-dimensional, and the *representations* and the *field content* are infinite-dimensional. A finite algebra is a generator and a value algebra, not a carrier of the full representation theory.

## Summary

The multipole tower is infinite and the biquaternion algebra is finite, and there is no contradiction. The tower is the decomposition of the infinite-dimensional space of angular functions, $L^2(S^2) = \bigoplus_{l\geq0} D^{(l)}$, and it is a property of the **field**, a function of position. The algebra is the finite-dimensional **value space**, of complex dimension four, isomorphic to $M_2(\mathbb{C})$, and it is a property of each individual value of the field.

As a rotation module the algebra is $\mathbb{B} = D^{(0)}\oplus D^{(1)}$: its center is the trivial representation and its vector part is the vector representation, with weights $0, 0, \pm1$ and character $2+2\cos\theta = \chi_0+\chi_1$. It contains no weight-$\pm2$ state and hence no $D^{(2)}$. Its elements can carry the monopole and the dipole, and no higher multipole. Its product cannot create higher multipoles either, because $\mathbf{u}\mathbf{v} = -\mathbf{u}\cdot\mathbf{v} + \mathbf{u}\times\mathbf{v}$ keeps only the $D^{(0)}$ and $D^{(1)}$ channels of $D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)}$; and its gradient satisfies $\boldsymbol{\nabla}\boldsymbol{\nabla} = -\Delta\,e_0$, so the composition of two derivatives also keeps only the trace.

The tower lives in the function space, in the symmetric traceless tensor powers $\operatorname{Sym}^l_0(D^{(1)})\cong D^{(l)}$, in the harmonic polynomials $r^lY_l^m$, in the differential-operator algebra, and in the universal enveloping algebra $U(\mathfrak{su}(2))$, all infinite-dimensional; and the multipole moments are functionals of the source, not elements of the value algebra. A general no-go statement follows by dimension counting: no finite-dimensional complex algebra on which the rotation group acts by automorphisms can contain $D^{(l)}$ for all $l$ as subquotients of its rotation module, because a finite-dimensional module has only finitely many composition factors and the $D^{(l)}$ are pairwise non-isomorphic. Enlarging the algebra buys finitely many higher orders and no more — $M_3(\mathbb{C})$ contains $D^{(0)}\oplus D^{(1)}\oplus D^{(2)}$ but costs the two-dimensional spinor module — and only an infinite-dimensional algebra carries the whole tower.

The finite algebra is finite because it is the local value space; the tower is infinite because the theory is a field theory. The quadrupole is not an algebra element because it is a feature of the field's angular map and not of the algebra of its values.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\dim_{\mathbb{C}} = 4$, $\cong M_2(\mathbb{C})$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$, $e_ie_j = -\delta_{ij}e_0+\epsilon_{ijk}e_k$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}} = \{Q_0e_0\}$ | Center of $\mathbb{B}$ (the scalars) |
| $\mathrm{Tr}(\cdot)$ | Matrix trace, $\mathrm{Tr}(e_0) = 2$ (the conventions article) |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde{\Lambda}\in\mathbb{H}_{\mathbb{B}}$, $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | Rotation rotor, acting by $\tilde{Q}\mapsto\tilde{\Lambda}\tilde{Q}\bar{\tilde{\Lambda}}$ |
| $D^{(l)}$ | Irreducible rotation representation, $\dim_{\mathbb{C}} D^{(l)} = 2l+1$ (Wigner's $D$) |
| $L^2(S^2) = \bigoplus_l D^{(l)}$ | Angular function space (infinite-dimensional) |
| $\operatorname{Sym}^l_0(D^{(1)})\cong D^{(l)}$ | Symmetric traceless $l$-th power of the vector part |
| $r^lY_l^m$ | Solid harmonics: the harmonic polynomials of degree $l$ |
| $D^{(1)}\otimes D^{(1)} = D^{(0)}\oplus D^{(1)}\oplus D^{(2)}$ | Clebsch–Gordan decomposition |
| $\boldsymbol{\nabla}\boldsymbol{\nabla} = -\Delta\,e_0$ | The truncated second gradient |
| $U(\mathfrak{su}(2))$ | Universal enveloping algebra (infinite-dimensional) |
| $S = \mathbb{B}\epsilon$ | Minimal left ideal: the two-dimensional spinor module, $\epsilon$ a nonzero idempotent |
| $q_{lm}$ | Multipole moment (a functional of the source) |
| $\chi_l(\theta)$ | Character of $D^{(l)}$; $\chi_0+\chi_1 = 2+2\cos\theta$ |

## Further Reading

- W. Fulton and J. Harris, *Representation Theory: A First Course* (Springer, 1991), for the irreducible representations $D^{(l)}$ of $SU(2)$ and the Clebsch–Gordan decomposition.
- B. C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the universal enveloping algebra, the Poincaré–Birkhoff–Witt theorem, and the infinite-dimensional representation theory.
- J.-P. Serre, *Lie Algebras and Lie Groups* (Springer, 1992), for the structure of Lie algebras, their enveloping algebras, and their modules.
- R. Carter, G. Segal, and I. Macdonald, *Lectures on Lie Groups and Lie Algebras* (Cambridge, 1995), for the representation theory of compact Lie groups and the classification of simple modules.
- M. E. Rose, *Elementary Theory of Angular Momentum* (Wiley, 1957), for the angular-momentum tower and its Clebsch–Gordan structure in physics.
- A. R. Edmonds, *Angular Momentum in Quantum Mechanics* (Princeton, 1957), for the multipole decomposition and the coupling of angular momenta.
- I. M. Gel'fand, R. A. Minlos, and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the infinite-dimensional representation theory of the rotation group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for $M_2(\mathbb{C})$, the biquaternion algebra, and the spinor module.
- C. Doran and A. Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor action and the representation content of the spacetime algebra.
