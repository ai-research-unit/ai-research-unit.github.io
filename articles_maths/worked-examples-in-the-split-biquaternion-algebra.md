
# __Worked Examples in the Split-Biquaternion Algebra__

## Introduction

This article is the computational companion to the article on the split biquaternion algebra. Its purpose is to display, on explicit elements, every construction that the algebraic articles state in general: the basis products, the four involutions and their fixed-point subspaces, the idempotents and the two minimal left ideals, explicit zero-divisor pairs, the four conjugations acting on a concrete element, and the realisation of the two quaternion halves.

The treatment is purely mathematical. Every number is recomputed before it is asserted, and the model used for the calculations is stated: a split biquaternion $\tilde{Q} = \tilde q + j \tilde q'$ with $\tilde q, \tilde q' \in \mathbb{H}$ is written as the pair of real quaternions $(\tilde q, \tilde q')$, with multiplication $(\tilde q_1, \tilde q'_1)(\tilde q_2, \tilde q'_2) = (\tilde q_1\tilde q_2 + \tilde q'_1\tilde q'_2,\ \tilde q_1\tilde q'_2 + \tilde q'_1\tilde q_2)$. No physics is invoked. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra, and the split complex algebra $\mathbb{D}$ from the article on split complex algebra, with its idempotents $\tilde\Pi_1 = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_2 = \tfrac{1}{2}(1 - j)$.

Throughout,
$$
\tilde{Q} = Q_t e_t + Q_x \vec e_x + Q_y \vec e_y + Q_z \vec e_z, \qquad Q_\mu = q_\mu + j q'_\mu \in \mathbb{D},
$$
with real $q_\mu, q'_\mu$, and the four conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (split complex), ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (Hermitian) and ${}^{\flat} = -{}^{*}$ (anti-Hermitian).

## The Algebra and Its Basis

The algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is eight-dimensional over $\mathbb{R}$, with the real basis

$$
1, \quad \vec e_x, \quad \vec e_y, \quad \vec e_z, \quad j, \quad j \vec e_x, \quad j \vec e_y, \quad j \vec e_z.
$$

The unit $j$ is central, $j^2 = +1$, and commutes with each $\vec e_\mu$, while the quaternion units satisfy $\vec e_x^2 = \vec e_y^2 = \vec e_z^2 = -1$ and $\vec e_x \vec e_y = \vec e_z$, $\vec e_y \vec e_z = \vec e_x$, $\vec e_z \vec e_x = \vec e_y$, with $\vec e_\mu \vec e_\nu = -\vec e_\nu \vec e_\mu$ for $\mu \neq \nu$. The products of the basis elements $\{1, \vec e_x, \vec e_y, \vec e_z\}$ are:

| | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
|---|---|---|---|---|
| $e_t$ | $e_t$ | $\vec e_x$ | $\vec e_y$ | $\vec e_z$ |
| $\vec e_x$ | $\vec e_x$ | $-e_t$ | $\vec e_z$ | $-\vec e_y$ |
| $\vec e_y$ | $\vec e_y$ | $-\vec e_z$ | $-e_t$ | $\vec e_x$ |
| $\vec e_z$ | $\vec e_z$ | $\vec e_y$ | $-\vec e_x$ | $-e_t$ |

The same table holds after replacing any entry by its product with $j$, since $j$ is central. In scalar-vector form, for $\tilde{Q}_1 = Q_{1t} e_t + \vec Q_1$ and $\tilde{Q}_2 = Q_{2t} e_t + \vec Q_2$,

$$
\tilde{Q}_1 \tilde{Q}_2 = \big(Q_{1t} Q_{2t} - (\vec Q_1, \vec Q_2)\big) e_t + Q_{1t} \vec Q_2 + Q_{2t} \vec Q_1 + [\vec Q_1, \vec Q_2],
$$

where $(\vec Q_1, \vec Q_2) = \sum_{k=1}^{3} Q_{1k} Q_{2k}$ and $[\vec Q_1, \vec Q_2]$ is the split-complex-linear cross product. The algebra is associative but not commutative, because $[\vec Q_1, \vec Q_2]$ need not vanish; it is not a division algebra, because it has zero divisors, as the examples below show.

### Worked Multiplication

As a final check of the product formula, the square of the concrete element is

$$
\boxed{\;
\tilde{Q}^2 = (-4 + 4 \vec e_x) + j (4 + 4 \vec e_x)
\;}.
$$

This can be verified either from the scalar-vector formula, using $Q_t = 1 + j$, $\vec Q = 2 \vec e_x + (1 - j) \vec e_y$, or from the idempotent components: since $\tilde\Pi_1^2 = \tilde\Pi_1$, $\tilde\Pi_2^2 = \tilde\Pi_2$ and $\tilde\Pi_1 \tilde\Pi_2 = 0$,

$$
\tilde{Q}^2 = \tilde{Q}_+^2 \tilde\Pi_1 + \tilde{Q}_-^2 \tilde\Pi_2,
$$

with $\tilde{Q}_+^2 = (2 + 2 \vec e_x)^2 = 4 + 8 \vec e_x + 4 \vec e_x^2 = 8 \vec e_x$ and $\tilde{Q}_-^2 = (2 \vec e_x + 2 \vec e_y)^2 = 4 \vec e_x^2 + 4(\vec e_x \vec e_y + \vec e_y \vec e_x) + 4 \vec e_y^2 = -8$, the cross terms cancelling. Reassembling,

$$
(8 \vec e_x) \tilde\Pi_1 + (-8) \tilde\Pi_2 = 4 \vec e_x (1 + j) - 4 (1 - j) = (-4 + 4 \vec e_x) + j (4 + 4 \vec e_x),
$$

which agrees with the value above. The agreement of the two routes illustrates the role of the idempotent decomposition as the computational shortcut of the algebra.

## A Concrete Element and Its Components

Take the concrete element

$$
\tilde{Q} = (1 + j) + 2 \vec e_x + (1 - j) \vec e_y = (1 + j) e_t + 2 \vec e_x + (1 - j) \vec e_y,
$$

so that the split complex coefficients are

$$
Q_t = 1 + j, \qquad Q_x = 2, \qquad Q_y = 1 - j, \qquad Q_z = 0.
$$

Writing $\tilde{Q} = \tilde q + j \tilde q'$ with $\tilde q, \tilde q' \in \mathbb{H}$ real quaternions, the real and split-imaginary parts are

$$
\tilde q = 1 + 2 \vec e_x + \vec e_y, \qquad \tilde q' = 1 - \vec e_y.
$$

The idempotent components are $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2} = (\tilde q \pm \tilde q') \tilde\Pi_{1,2}$, and since $\tilde q + \tilde q' = 2 + 2 \vec e_x$ and $\tilde q - \tilde q' = 2 \vec e_x + 2 \vec e_y$,

$$
\tilde{Q}_+ = 2 + 2 \vec e_x, \qquad \tilde{Q}_- = 2 \vec e_x + 2 \vec e_y.
$$

Both components are nonzero, so $\tilde{Q}$ is a unit.

## The Four Conjugations on a Concrete Element

Applying the four conjugations to $\tilde{Q} = (1 + j) + 2 \vec e_x + (1 - j) \vec e_y$ gives the following explicit elements:

- quaternion conjugation $\tilde{Q}^{\natural} = (1 + j) - 2 \vec e_x - (1 - j) \vec e_y$, obtained by negating the vector part;
- split complex conjugation $\bar{\tilde{Q}} = (1 - j) + 2 \vec e_x + (1 + j) \vec e_y$, obtained by conjugating each coefficient, $j \mapsto -j$;
- Hermitian conjugation $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}} = (1 - j) - 2 \vec e_x - (1 + j) \vec e_y$;
- anti-Hermitian conjugation $\tilde{Q}^\flat = -\tilde{Q}^{*} = -(1 - j) + 2 \vec e_x + (1 + j) \vec e_y$.

Each is an involution: applying it twice returns $\tilde{Q}$. For instance $\bar{\tilde{Q}^{\natural}} = \bar{(1 + j) - 2 \vec e_x - (1 - j) \vec e_y} = (1 + j) + 2 \vec e_x + (1 - j) \vec e_y = \tilde{Q}$, and the same holds for the other three.

## The Four Involution Fixed-Point Subspaces

Each conjugation has a fixed-point subspace, and the projection onto the fixed-point subspace of an involution $\sigma$, along the complementary eigenspace, is $\tfrac{1}{2}(\tilde{Q} + \sigma \tilde{Q})$. The four subspaces are listed below, with their defining conditions and real dimensions.

| Involution | Fixed subspace | Condition | Dimension |
|---|---|---|---|
| ${}^{\natural}$ | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $Q_x = Q_y = Q_z = 0$ | $2$ |
| $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $q'_\mu = 0$ for all $\mu$ | $4$ |
| ${}^{*}$ | $\mathbb{M}_+$ | $q_t$ real and $Q_x, Q_y, Q_z$ purely split-imaginary | $4$ |
| ${}^{\flat}$ | $\mathbb{M}_-$ | $Q_t$ purely split-imaginary and $q_x, q_y, q_z$ real | $4$ |

Projecting $\tilde{Q}$ onto the four fixed-point subspaces gives

$$
\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural}) = 1 + j = Q_t \in \mathbb{D}_{\mathbb{H}_{\mathbb{D}}},
$$

$$
\tfrac{1}{2}(\tilde{Q} + \bar{\tilde{Q}}) = 1 + 2 \vec e_x + \vec e_y = \tilde q \in \mathbb{H}_{\mathbb{H}_{\mathbb{D}}},
$$

$$
\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{*}) = 1 - j \vec e_y \in \mathbb{M}_+,
$$

$$
\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^\flat) = (2 \vec e_x + \vec e_y) + j \in \mathbb{M}_-.
$$

The four projections do not sum to $\tilde{Q}$: the four subspaces overlap — for example $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{R}$, the real scalars — so they are four distinct fixed-point sets rather than the four summands of a single decomposition.

## The Idempotents and the Two Minimal Left Ideals

The idempotents of $\mathbb{H}_{\mathbb{D}}$ are $0, \tilde\Pi_1, \tilde\Pi_2, 1$, with

$$
\tilde\Pi_1 = \tfrac{1}{2}(1 + j), \qquad \tilde\Pi_2 = \tfrac{1}{2}(1 - j), \qquad \tilde\Pi_1 \tilde\Pi_2 = 0, \qquad \tilde\Pi_1 + \tilde\Pi_2 = 1.
$$

They are central and primitive, and they give the idempotent decomposition

$$
\boxed{\;
\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_1 \oplus \mathbb{H} \tilde\Pi_2, \qquad \mathbb{H} \tilde\Pi_{1,2} = \{ \tilde{Q} \tilde\Pi_{1,2} : \tilde{Q} \in \mathbb{H}_{\mathbb{D}} \} \cong \mathbb{H}
\;},
$$

into the two minimal left ideals, each of real dimension $4$. On the concrete element the decomposition reads

$$
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_1 + \tilde{Q}_- \tilde\Pi_2 = (2 + 2 \vec e_x) \tilde\Pi_1 + (2 \vec e_x + 2 \vec e_y) \tilde\Pi_2.
$$

Because $\tilde\Pi_{1,2}$ are central, $\mathbb{H} \tilde\Pi_1$ and $\mathbb{H} \tilde\Pi_2$ are two-sided ideals as well: they are the two quaternion halves of the algebra.

## Explicit Zero Divisors

The simplest zero-divisor pair is the idempotent pair $\tilde\Pi_1 \tilde\Pi_2 = 0$, with both factors nonzero. A less trivial pair is obtained by taking an element of one half and an element of the other:

$$
\tilde{Q}_1 = \vec e_x \tilde\Pi_2, \qquad \tilde{Q}_2 = (1 + \vec e_y) \tilde\Pi_1.
$$

In developed form,

$$
\tilde{Q}_1 = \tfrac{1}{2} \vec e_x (1 - j) = \tfrac{1}{2} \vec e_x - \tfrac{1}{2} j \vec e_x, \qquad \tilde{Q}_2 = \tfrac{1}{2}(1 + \vec e_y)(1 + j) = \tfrac{1}{2}(1 + j) + \tfrac{1}{2}(1 + j) \vec e_y.
$$

Since $\tilde\Pi_2 \tilde\Pi_1 = 0$ and $\vec e_x (1 + \vec e_y) = \vec e_x + \vec e_x \vec e_y = \vec e_x + \vec e_z$ is a quaternion,

$$
\boxed{\;
\tilde{Q}_1 \tilde{Q}_2 = \vec e_x (1 + \vec e_y) \tilde\Pi_2 \tilde\Pi_1 = 0
\;},
$$

while neither $\tilde{Q}_1$ nor $\tilde{Q}_2$ is zero. The pair therefore exhibits an explicit zero divisor, and it shows the general shape of the zero divisor set: the zero divisors of $\mathbb{H}_{\mathbb{D}}$ are exactly the elements with $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$, that is, the union of the two halves $\mathbb{H} \tilde\Pi_2 \cup \mathbb{H} \tilde\Pi_1$. The classification is developed in *Split-Biquaternion Zero Divisors*.

## The Two Quaternion Halves Realised

The isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$, sends the concrete element to

$$
\varphi(\tilde{Q}) = \big(2 + 2 \vec e_x, \; 2 \vec e_x + 2 \vec e_y \big).
$$

Multiplication is componentwise, so the concrete element is a unit in $\mathbb{H}_{\mathbb{D}}$ exactly because each of $2 + 2 \vec e_x$ and $2 \vec e_x + 2 \vec e_y$ is a nonzero quaternion, hence a unit in $\mathbb{H}$; indeed

$$
(2 + 2 \vec e_x)^{-1} = \tfrac{1}{8}(2 - 2 \vec e_x), \qquad (2 \vec e_x + 2 \vec e_y)^{-1} = \tfrac{1}{8}(-2 \vec e_x - 2 \vec e_y),
$$

and $\varphi(\tilde{Q}^{-1}) = \tfrac{1}{8}(2 - 2 \vec e_x, -2 \vec e_x - 2 \vec e_y)$, which agrees with the inverse $\tilde{Q}^{-1} = \tfrac{1}{8} \tilde{Q}^{\natural}$. The two halves are thus not merely an abstract direct sum: on this element they are the two nonzero quaternions whose product-freeness decides invertibility.

## Summary

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ has the real basis $1, \vec e_x, \vec e_y, \vec e_z, j, j \vec e_x, j \vec e_y, j \vec e_z$ and the product formula $\tilde{Q}_1 \tilde{Q}_2 = (Q_{1t} Q_{2t} - (\vec Q_1, \vec Q_2)) e_t + Q_{1t} \vec Q_2 + Q_{2t} \vec Q_1 + [\vec Q_1, \vec Q_2]$. On the concrete element

$$
\tilde{Q} = (1 + j) + 2 \vec e_x + (1 - j) \vec e_y
$$

the four conjugations act as $\tilde{Q}^{\natural} = (1 + j) - 2 \vec e_x - (1 - j) \vec e_y$, $\bar{\tilde{Q}} = (1 - j) + 2 \vec e_x + (1 + j) \vec e_y$, $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ and $\tilde{Q}^\flat = -\tilde{Q}^{*}$; the four fixed-point subspaces $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ have dimensions $2, 4, 4, 4$ and overlap, so their projections do not sum to the element. The idempotents $\tilde\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ are central and primitive and give the two minimal left ideals $\mathbb{H} \tilde\Pi_{1,2}$; the element decomposes as $\tilde{Q} = (2 + 2 \vec e_x) \tilde\Pi_1 + (2 \vec e_x + 2 \vec e_y) \tilde\Pi_2$ with both components nonzero. An explicit zero-divisor pair is $\tilde{Q}_1 = \vec e_x \tilde\Pi_2$ and $\tilde{Q}_2 = (1 + \vec e_y) \tilde\Pi_1$, with $\tilde{Q}_1 \tilde{Q}_2 = 0$. The isomorphism $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-) = (2 + 2 \vec e_x, 2 \vec e_x + 2 \vec e_y)$ realises the two quaternion halves, and the square $\tilde{Q}^2 = (-4 + 4 \vec e_x) + j(4 + 4 \vec e_x)$ agrees whether computed from the product formula or from the idempotent components.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, $\cong \mathbb{H} \oplus \mathbb{H}$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis |
| $j$ | Split complex unit, central, $j^2 = +1$ |
| $\tilde\Pi_{1,2} = \tfrac{1}{2}(1 \pm j)$ | The idempotents, $\tilde\Pi_1 + \tilde\Pi_2 = 1$ |
| $\tilde{Q} = \tilde q + j \tilde q'$ | Concrete element, $\tilde q, \tilde q' \in \mathbb{H}$ |
| $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_{1,2}$ | Idempotent components in $\mathbb{H}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | The four involution fixed-point subspaces |
| $\mathbb{H} \tilde\Pi_{1,2}$ | The two minimal left ideals, each $\cong \mathbb{H}$ |
| $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$ | Idempotent-decomposition isomorphism |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion multiplication table and the scalar-vector product formula.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic biquaternion calculus.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for worked computations in the split biquaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the idempotent basis and the direct-sum structure of Clifford algebras of split signature.
