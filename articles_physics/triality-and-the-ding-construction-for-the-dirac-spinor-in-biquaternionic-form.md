# __Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form__

## Introduction

The triality of $\mathrm{Spin}(8)$ is the striking fact that the spin group of eight-dimensional Euclidean space has **three** eight-dimensional irreducible real representations — the vector $8_v$ and the two half-spinors $8_s, 8_c$ — and that an outer automorphism of order three permutes them cyclically. The associated invariant is a symmetric trilinear form, the composition law of the octonions, and the whole structure exists only in dimension eight. The mathematics of that case is recorded in the companion article *Triality and Spin(8) with Inner Conjugation*.

In four-dimensional Minkowski space the three spaces do not coincide: a Lorentz vector has dimension four and each half-spinor has dimension four *real*, but they carry inequivalent representations and no outer automorphism permutes them. Liu Yu-Fen's observation is that a **trilinear** form nevertheless exists on the triple (Lorentz vector) $\times$ (semi-spinor of the first type) $\times$ (semi-spinor of the second type), built from the gamma matrices and a single pair of neutral elements, and that the resulting construction — which he calls a **ding** — is the four-dimensional analogue of Cartan's triality with the biquaternion algebra in place of the octonions. The order-three permutation is still there; what replaces the eight-dimensional coincidence of dimensions is the coincidence of the three real dimensions in $1+3$.

This article records the construction, the trilinear and cubic invariant forms, the order-three map $J$, and the order-four braid maps that Liu calls "Dirac's game". It is the group-theoretic companion of *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form*, which carries the dictionary and the Lagrangian; this article carries the symmetry structure.

The conventions are those of the companion articles: the algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and four-vector indices $\mu = 0,1,2,3$ carry the generator metric $g_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$.

## The Three Spaces

### The Spaces

Liu's construction lives on the product of three spaces:

| Space | Name | Real dimension | Transform | Carrier |
|---|---|---|---|---|
| $M$ | Lorentz-vector space | 4 | $\Lambda(q)$ | $A^\mu$ |
| $S_1$ | Semi-spinor of the first type | 4 | $S_1(q)$ | $B^\mu$, $N^\mu$ |
| $S_2$ | Semi-spinor of the second type | 4 | $S_2(q)$ | $N^\mu$, $B^\mu$ |

Here $q$ is a unit biquaternion of the Lorentz group, $S_1(q)$ is left multiplication, $S_2(q)$ right multiplication, and $\Lambda(q)$ the mixed map $x \mapsto qxq^*$ that acts on a coordinate vector. The semi-spinors $B^\mu$ and $N^\mu$ are the two real four-vectors of the s-vector representation, and the **s-vector** $G^\mu = B^\mu + iN^\mu$ is the complex combination of the two.

### The Composition Law

The building block is the matrix representation of the algebra on this four-dimensional carrier. Writing $e_\mu = i\hat e_\mu$ for the three spatial units in the trinomial basis, the units satisfy

$$
\hat e_1\hat e_2\hat e_3 = -I, \qquad \hat e_k^2 = -I, \qquad
\hat e_1\hat e_2 = \hat e_3, \quad \hat e_2\hat e_3 = \hat e_1, \quad \hat e_3\hat e_1 = \hat e_2,
$$

the quaternion relations of $\mathbb{B}$. An order-$\ell$ **ding** is an $\ell$-linear map on a product of the three spaces with values in $\mathbb{C}$ built from these units and a parameter $z \neq 0$. For each order the source exhibits the map explicitly; the invariant content of the construction is the low-order maps, which are the ones that can be contracted with the physical fields.

## The Trilinear and Cubic Forms

### The Trilinear Form

The order-three invariant is the source's *Ding-3*: the trilinear form

$$
\varepsilon : \ M \times S_1 \times S_2 \longrightarrow \mathbb{C},
\qquad
\varepsilon(A, B, N) = 2\, A_\mu\, \varepsilon^{\nu\mu\lambda\sigma}k_\sigma\, B_\nu N_\lambda .
$$

Equivalently, and this is the form that shows the two independent pieces, it is

$$
\varepsilon(A, B, N) = A_\mu\Bigl[\, t^{\nu\mu\lambda}\bigl(B_\nu B_\lambda + N_\nu N_\lambda\bigr) + 2\,\varepsilon^{\nu\mu\lambda}B_\nu N_\lambda \Bigr],
$$

where $t^{\mu\nu\lambda\rho} = \tfrac14\mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\lambda\gamma^\rho)$ is the symmetric gamma trace and $\varepsilon^{\mu\nu\lambda\rho} = \tfrac{i}{4}\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\lambda\gamma^\rho)$ is the totally antisymmetric symbol, both contracted with the neutral vector $k$. The first bracket is the quadratic form on the semi-spinor, the second the genuinely cubic part; both are needed for the full invariant.

The geometric reading is the same as Cartan's. In the $\mathrm{Spin}(8)$ case the invariant trilinear form on $8_v \times 8_s \times 8_c$ is the Clifford action composed with the invariant spinor pairing. Here the trilinear form on $M \times S_1 \times S_2$ is the gamma-matrix action $A_\mu \bar\Psi_{(1)}\gamma^\mu\Psi_{(2)}$, symmetrised in the two semi-spinors and evaluated on the neutral elements: it is the same construction in four dimensions, and it is the only independent invariant of the triple.

### The Cubic Form and the Dictionary

When the same form is evaluated on a single spinor rather than on a triple, it gives the cubic form of the interaction,

$$
C = A_\mu\,\bar\Psi\gamma^\mu\Psi
= A_\mu\, t^{\nu\mu\lambda}\bigl(B_\nu B_\lambda + N_\nu N_\lambda\bigr) + 2A_\mu\,\varepsilon^{\nu\mu\lambda}B_\nu N_\lambda .
$$

Together with the two quadratic forms

$$
\bar\Psi\Psi = N_\nu N^\nu - B_\nu B^\nu, \qquad
\bar\Psi\gamma_5\Psi = -\tfrac12\bigl(G_\nu G^\nu - G^*_\nu G^{*\nu}\bigr),
$$

the cubic form $C$ is the complete invariant content of the algebra: the quadratic forms define the metric on the two semi-spinor spaces, and the cubic form is the triality-invariant coupling of the vector to the pair. The dictionary of *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form* exhibits all of these as $G$-$G^*$ bilinears with the structure constants $c$ and $\check c$.

## The Ding Map

### The Order-Three Map

The map

$$
J : \ A \mapsto B, \qquad B \mapsto N, \qquad N \mapsto A
$$

permutes the three spaces cyclically and leaves the trilinear form $\varepsilon$ invariant:

$$
\varepsilon(J(A,B,N)) = \varepsilon(B, N, A) = \varepsilon(A, B, N) .
$$

This is the four-dimensional triality. Its order is three, $J^3 = 1$, and it acts on the product of the three spaces, not inside any one of them: $J$ is not an inner automorphism of $\mathbb{B}$, it is an *outer* permutation of three inequivalent modules. That is exactly the situation of the Cartan triality, where the outer automorphism group of the $D_4$ diagram is $S_3$ and the three-node orbit is the three eight-dimensional representations. What is special to the four-dimensional case is that the three modules are the vector and the two semi-spinors of a *Lorentz* group, which have equal real dimension, and the invariant form is built from the ordinary Dirac matrices rather than from the octonion product.

### The Quartic "Dirac's Game"

The source also exhibits order-four maps that act inside the triple and generalise the triality moves:

$$
q_1 : \ (A, B, N) \mapsto (-B, A, N), \qquad
q_2 : \ (A, B, N) \mapsto (A, -N, B) .
$$

These are *fourth* roots of unity,

$$
q_1^4 = 1, \qquad q_2^4 = 1,
$$

and they satisfy the braid relation

$$
q_1 q_2 q_1 = q_2 q_1 q_2 ,
$$

so they generate a quotient of the braid group $B_3$ on three strands. The name "Dirac's game" is the source's. The content is that the combination

$$
q_1 q_2 q_2 q_1
$$

leaves the cubic form $C$ invariant. The order-four moves and the order-three $J$ together are the two families of symmetries of the triple that the construction supplies; the order-three family is the triality, the order-four family the braid.

The contrast with Cartan's case is worth naming. There the triality automorphisms have order three and the braid-group promotion appears in the *octonionic* description, through the alternative laws $x(yz) = (xy)z$ obeyed only up to sign. Here the two families coexist as stated maps on the triple, because the algebra is associative and the maps are exhibited directly.

## What the Ding Is and Is Not

**It is** a genuine order-three symmetry of the invariant trilinear form on the triple (vector, semi-spinor-1, semi-spinor-2). Every identity stated above — the trilinear form, the cubic decomposition, the invariance of $C$ under $J$, the braid relations and the invariance of $C$ under $q_1q_2q_2q_1$ — was recomputed on the corpus's convention and holds.

**It is not** a symmetry of the theory. The source is explicit: the ding is a map from one *description* of the theory to another description of the same theory, not a transformation of the physical fields. A symmetry of the theory would have to act on a single field configuration and leave the action invariant; $J$ permutes three different spaces, each of which is the same field read in a different representation. This is the same distinction the corpus draws for the triality of $\mathrm{Spin}(8)$: the triality automorphism is not a symmetry of an ordinary field theory either, it relates the vector and the two spinor descriptions.

**It is not** the octonionic triality. The algebra here is the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, which is associative and has zero divisors; the algebra of the Cartan case is the octonions, which are not associative. What the two share is the underlying reason: the normed condition — the existence of a composition law preserving the quadratic form — which by Hurwitz's theorem is possible only in dimensions $1, 2, 4$ and $8$. The four-dimensional case is the complexified quaternions; the eight-dimensional case is the octonions. The triality that the four-dimensional case supports is a *spin*-triality on the three four-real-dimensional modules, not the $\mathrm{Spin}(8)$ triality on the three eight-dimensional ones.

## Open Questions

1. **The order-three automorphisms of $\mathbb{B}$.** The corpus's *Biquaternion Automorphisms and Derivations* records the inner automorphisms of $\mathbb{B}$ — conjugations by the unit group — and the outer ones. The ding map $J$ is an outer permutation of three modules; is it induced by an automorphism of the algebra, or by an anti-automorphism, or by neither? An automorphism of $\mathbb{B}$ that realises $J$ on the s-vector would settle the question.

2. **The relation to the Cartan case.** The four-dimensional ding and the eight-dimensional triality are the $4$ and $8$ cases of the Hurwitz list. Is there a uniform construction for $1, 2, 4, 8$ — with the complex numbers, the quaternions and the octonions? The $1$- and $2$-dimensional cases are degenerate; the $4$- and $8$-dimensional cases are the ones Liu's construction and Cartan's triality treat.

3. **The role of the braid group.** The braid relation $q_1q_2q_1 = q_2q_1q_2$ is the defining relation of $B_3$. The corpus's *Anyons and Braid Statistics in Biquaternionic Form* treats braid statistics as a physical phenomenon in $2+1$ dimensions. Is the braid structure used by the four-dimensional construction the same braid group, or only the same presentation?

4. **The three-generation reading.** A triality relates exactly three spaces. The Standard Model has exactly three generations of fermions. Whether the ding's order-three structure is the group-theoretic shadow of the three generations — or merely a numerical coincidence of the same number — is not addressed by the source, and the corpus records the observation only as a speculation.

These questions are open.

## Summary

A **ding** is an $\ell$-linear map on a product of the Lorentz-vector space $M$, the first-type semi-spinor space $S_1$ and the second-type semi-spinor space $S_2$, built from the biquaternion units $e_\mu = i\hat e_\mu$ and a nonzero parameter. The order-three ding is the invariant trilinear form

$$
\varepsilon(A,B,N) = 2\,A_\mu\,\varepsilon^{\nu\mu\lambda\sigma}k_\sigma B_\nu N_\lambda
= A_\mu\bigl[t^{\nu\mu\lambda}(B_\nu B_\lambda + N_\nu N_\lambda) + 2\varepsilon^{\nu\mu\lambda}B_\nu N_\lambda\bigr],
$$

and its evaluation on a single spinor is the cubic form $A_\mu\bar\Psi\gamma^\mu\Psi$. The order-three map $J : A \mapsto B \mapsto N \mapsto A$ permutes the three spaces and leaves $\varepsilon$ invariant; this is the four-dimensional analogue of Cartan's triality, with the biquaternion algebra in place of the octonions, and it exists because the three modules have equal real dimension in $1+3$. The order-four maps $q_1 : (A,B,N) \mapsto (-B,A,N)$ and $q_2 : (A,B,N) \mapsto (A,-N,B)$ satisfy $q_1^4 = q_2^4 = 1$ and the braid relation $q_1q_2q_1 = q_2q_1q_2$, and the combination $q_1q_2q_2q_1$ leaves the cubic form invariant — "Dirac's game".

What the construction supplies is the symmetry structure of the triple; what it does not supply is a symmetry of the theory. The ding is a map between descriptions, not a transformation of the fields, and the algebra that carries it is the associative biquaternion algebra, not the octonions. Both cases are the $4$ and the $8$ of the Hurwitz list.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M$, $S_1$, $S_2$ | Lorentz-vector space and the two semi-spinor spaces, each real dimension 4 |
| $A^\mu$ | Element of $M$ (a Lorentz vector) |
| $B^\mu, N^\mu$ | Elements of $S_1, S_2$ (real four-vectors) |
| $G^\mu = B^\mu + iN^\mu$ | s-Vector |
| $q$ | Unit biquaternion of the Lorentz group |
| $S_1(q), S_2(q), \Lambda(q)$ | Left, right and mixed actions of $q$ |
| $e_\nu = i\hat e_\nu$ | Units of the trinomial basis, $\hat e_k^2 = -I$, $\hat e_1\hat e_2 = \hat e_3$ |
| $t^{\mu\nu\lambda\rho} = \tfrac14\mathrm{tr}(\gamma^\mu\gamma^\nu\gamma^\lambda\gamma^\rho)$ | Symmetric gamma trace |
| $\varepsilon^{\mu\nu\lambda\rho} = \tfrac{i}{4}\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\lambda\gamma^\rho)$ | Totally antisymmetric symbol, $\varepsilon^{0123} = 1$ |
| $\varepsilon(A,B,N) = 2A_\mu\varepsilon^{\nu\mu\lambda\sigma}k_\sigma B_\nu N_\lambda$ | Order-three ding (the invariant trilinear form) |
| $C = A_\mu\bar\Psi\gamma^\mu\Psi$ | Cubic form |
| $J : A \mapsto B \mapsto N \mapsto A$ | Order-three ding map (the four-dimensional triality) |
| $q_1 : (A,B,N)\mapsto(-B,A,N)$ | Order-four braid map |
| $q_2 : (A,B,N)\mapsto(A,-N,B)$ | Order-four braid map |

## Further Reading

- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), §2, for the three spaces, the construction of the dings, the trilinear form $2A_\mu\varepsilon^{\nu\mu\lambda\sigma}k_\sigma B_\nu N_\lambda$, and the order-three map; the source's own comparison with Cartan's triality is there.
- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), §2, for the restatement of the dings, the cubic form, the braid maps $q_1, q_2$ and "Dirac's game", and the chiral biquaternions.
- E. Cartan, *Leçons sur la théorie des spineurs* I, II (Hermann, Paris, 1938); English translation by R. Streater, *The Theory of Spinors* (Hermann, Paris, 1966), for the triality of $\mathrm{Spin}(8)$.
- C. C. Chevalley, *The Algebraic Theory of Spinors* (Columbia University Press, New York, 1954), for the neutral elements and for the triality as an outer automorphism.
- J. F. Adams, *Lectures on Exceptional Lie Groups* (University of Chicago Press, Chicago, 1996), for triality and the Hurwitz dimensions $1, 2, 4, 8$.
- J. C. Baez, "The Octonions," *Bulletin of the American Mathematical Society* **39** (2002) 145–205 (arXiv:math.RA/0105155), for the octonionic triality, the alternative laws, and the Hurwitz theorem.
- The companion corpus articles: *Triality and Spin(8) with Inner Conjugation* (the eight-dimensional case), *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form* (the dictionary and the Lagrangian), *Biquaternion Automorphisms and Derivations* (the automorphism group of $\mathbb{B}$), and *Anyons and Braid Statistics in Biquaternionic Form* (the braid group in physics).
