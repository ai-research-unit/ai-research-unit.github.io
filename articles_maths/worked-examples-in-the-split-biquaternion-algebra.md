
# __Worked Examples in the Split-Biquaternion Algebra__

## Introduction

This article is the computational companion to the article on the split biquaternion algebra. Its purpose is to display, on explicit elements, every construction that the algebraic articles state in general: the basis products, the four involutions and their fixed-point subspaces, the idempotents and the two minimal left ideals, explicit zero-divisor pairs, the four conjugations acting on a concrete element, and the realisation of the two quaternion halves.

The treatment is purely mathematical. Every number is recomputed before it is asserted, and the model used for the calculations is stated: a split biquaternion $\tilde{Q} = A + j B$ with $A, B \in \mathbb{H}$ is written as the pair of real quaternions $(A, B)$, with multiplication $(A, B)(C, D) = (AC + BD, AD + BC)$. No physics is invoked. The quaternion algebra $\mathbb{H}$ is assumed from the article on quaternion algebra, and the split complex algebra $\mathbb{D}$ from the article on split complex algebra, with its idempotents $\tilde\Pi_+ = \tfrac{1}{2}(1 + j)$ and $\tilde\Pi_- = \tfrac{1}{2}(1 - j)$.

Throughout,
$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu = q_\mu + j q'_\mu \in \mathbb{D},
$$
with real $q_\mu, q'_\mu$, and the four conjugations are ${}^{\natural}$ (quaternion), $\bar{\cdot}$ (split complex), ${}^{*} = \bar{\cdot}\circ{}^{\natural}$ (Hermitian) and ${}^{\flat} = -{}^{*}$ (anti-Hermitian).

## The Algebra and Its Basis

The algebra $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ is eight-dimensional over $\mathbb{R}$, with the real basis

$$
1, \quad e_1, \quad e_2, \quad e_3, \quad j, \quad j e_1, \quad j e_2, \quad j e_3.
$$

The unit $j$ is central, $j^2 = +1$, and commutes with each $e_k$, while the quaternion units satisfy $e_1^2 = e_2^2 = e_3^2 = -1$ and $e_1 e_2 = e_3$, $e_2 e_3 = e_1$, $e_3 e_1 = e_2$, with $e_k e_l = -e_l e_k$ for $k \neq l$. The products of the basis elements $\{1, e_1, e_2, e_3\}$ are:

| | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|---|
| $e_0$ | $e_0$ | $e_1$ | $e_2$ | $e_3$ |
| $e_1$ | $e_1$ | $-e_0$ | $e_3$ | $-e_2$ |
| $e_2$ | $e_2$ | $-e_3$ | $-e_0$ | $e_1$ |
| $e_3$ | $e_3$ | $e_2$ | $-e_1$ | $-e_0$ |

The same table holds after replacing any entry by its product with $j$, since $j$ is central. In scalar-vector form, for $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ and $\tilde{R} = R_0 e_0 + \mathbf{R}$,

$$
\tilde{Q} \tilde{R} = \big(Q_0 R_0 - (\mathbf{Q}, \mathbf{R})\big) e_0 + Q_0 \mathbf{R} + R_0 \mathbf{Q} + [\mathbf{Q}, \mathbf{R}],
$$

where $(\mathbf{Q}, \mathbf{R}) = \sum_{k=1}^{3} Q_k R_k$ and $[\mathbf{Q}, \mathbf{R}]$ is the split-complex-linear cross product. The algebra is associative but not commutative, because $[\mathbf{Q}, \mathbf{R}]$ need not vanish; it is not a division algebra, because it has zero divisors, as the examples below show.

### Worked Multiplication

As a final check of the product formula, the square of the concrete element is

$$
\tilde{Q}^2 = (-4 + 4 e_1) + j (4 + 4 e_1).
$$

This can be verified either from the scalar-vector formula, using $Q_0 = 1 + j$, $\mathbf{Q} = 2 e_1 + (1 - j) e_2$, or from the idempotent components: since $\tilde\Pi_+^2 = \tilde\Pi_+$, $\tilde\Pi_-^2 = \tilde\Pi_-$ and $\tilde\Pi_+ \tilde\Pi_- = 0$,

$$
\tilde{Q}^2 = \tilde{Q}_+^2 \tilde\Pi_+ + \tilde{Q}_-^2 \tilde\Pi_-,
$$

with $\tilde{Q}_+^2 = (2 + 2 e_1)^2 = 4 + 8 e_1 + 4 e_1^2 = 8 e_1$ and $\tilde{Q}_-^2 = (2 e_1 + 2 e_2)^2 = 4 e_1^2 + 4(e_1 e_2 + e_2 e_1) + 4 e_2^2 = -8$, the cross terms cancelling. Reassembling,

$$
(8 e_1) \tilde\Pi_+ + (-8) \tilde\Pi_- = 4 e_1 (1 + j) - 4 (1 - j) = (-4 + 4 e_1) + j (4 + 4 e_1),
$$

which agrees with the value above. The agreement of the two routes illustrates the role of the idempotent decomposition as the computational shortcut of the algebra.

## A Concrete Element and Its Components

Take the concrete element

$$
\tilde{Q} = (1 + j) + 2 e_1 + (1 - j) e_2 = (1 + j) e_0 + 2 e_1 + (1 - j) e_2,
$$

so that the split complex coefficients are

$$
Q_0 = 1 + j, \qquad Q_1 = 2, \qquad Q_2 = 1 - j, \qquad Q_3 = 0.
$$

Writing $\tilde{Q} = A + j B$ with $A, B \in \mathbb{H}$ real quaternions, the real and split-imaginary parts are

$$
A = 1 + 2 e_1 + e_2, \qquad B = 1 - e_2.
$$

The idempotent components are $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_\pm = (A \pm B) \tilde\Pi_\pm$, and since $A + B = 2 + 2 e_1$ and $A - B = 2 e_1 + 2 e_2$,

$$
\tilde{Q}_+ = 2 + 2 e_1, \qquad \tilde{Q}_- = 2 e_1 + 2 e_2.
$$

Both components are nonzero, so $\tilde{Q}$ is a unit.

## The Four Conjugations on a Concrete Element

Applying the four conjugations to $\tilde{Q} = (1 + j) + 2 e_1 + (1 - j) e_2$ gives the following explicit elements:

- quaternion conjugation $\tilde{Q}^{\natural} = (1 + j) - 2 e_1 - (1 - j) e_2$, obtained by negating the vector part;
- split complex conjugation $\bar{\tilde{Q}} = (1 - j) + 2 e_1 + (1 + j) e_2$, obtained by conjugating each coefficient, $j \mapsto -j$;
- Hermitian conjugation $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}} = (1 - j) - 2 e_1 - (1 + j) e_2$;
- anti-Hermitian conjugation $\tilde{Q}^\flat = -\tilde{Q}^{*} = -(1 - j) + 2 e_1 + (1 + j) e_2$.

Each is an involution: applying it twice returns $\tilde{Q}$. For instance $\bar{\tilde{Q}^{\natural}} = \bar{(1 + j) - 2 e_1 - (1 - j) e_2} = (1 + j) + 2 e_1 + (1 - j) e_2 = \tilde{Q}$, and the same holds for the other three.

## The Four Involution Fixed-Point Subspaces

Each conjugation has a fixed-point subspace, and the projection onto the fixed-point subspace of an involution $\sigma$, along the complementary eigenspace, is $\tfrac{1}{2}(\tilde{Q} + \sigma \tilde{Q})$. The four subspaces are listed below, with their defining conditions and real dimensions.

| Involution | Fixed subspace | Condition | Dimension |
|---|---|---|---|
| ${}^{\natural}$ | $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$ | $Q_1 = Q_2 = Q_3 = 0$ | $2$ |
| $\bar{\cdot}$ | $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | $q'_\mu = 0$ for all $\mu$ | $4$ |
| ${}^{*}$ | $\mathbb{M}_+$ | $q_0$ real and $Q_1, Q_2, Q_3$ purely split-imaginary | $4$ |
| ${}^{\flat}$ | $\mathbb{M}_-$ | $Q_0$ purely split-imaginary and $q_1, q_2, q_3$ real | $4$ |

Projecting $\tilde{Q}$ onto the four fixed-point subspaces gives

$$
\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{\natural}) = 1 + j = Q_0 \in \mathbb{D}_{\mathbb{H}_{\mathbb{D}}},
$$

$$
\tfrac{1}{2}(\tilde{Q} + \bar{\tilde{Q}}) = 1 + 2 e_1 + e_2 = A \in \mathbb{H}_{\mathbb{H}_{\mathbb{D}}},
$$

$$
\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^{*}) = 1 - j e_2 \in \mathbb{M}_+,
$$

$$
\tfrac{1}{2}(\tilde{Q} + \tilde{Q}^\flat) = (2 e_1 + e_2) + j \in \mathbb{M}_-.
$$

The four projections do not sum to $\tilde{Q}$: the four subspaces overlap — for example $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}} \cap \mathbb{H}_{\mathbb{H}_{\mathbb{D}}} = \mathbb{R}$, the real scalars — so they are four distinct fixed-point sets rather than the four summands of a single decomposition.

## The Idempotents and the Two Minimal Left Ideals

The idempotents of $\mathbb{H}_{\mathbb{D}}$ are $0, \tilde\Pi_+, \tilde\Pi_-, 1$, with

$$
\tilde\Pi_+ = \tfrac{1}{2}(1 + j), \qquad \tilde\Pi_- = \tfrac{1}{2}(1 - j), \qquad \tilde\Pi_+ \tilde\Pi_- = 0, \qquad \tilde\Pi_+ + \tilde\Pi_- = 1.
$$

They are central and primitive, and they give the idempotent decomposition

$$
\mathbb{H}_{\mathbb{D}} = \mathbb{H} \tilde\Pi_+ \oplus \mathbb{H} \tilde\Pi_-, \qquad \mathbb{H} \tilde\Pi_\pm = \{ \tilde{R} \tilde\Pi_\pm : \tilde{R} \in \mathbb{H}_{\mathbb{D}} \} \cong \mathbb{H},
$$

into the two minimal left ideals, each of real dimension $4$. On the concrete element the decomposition reads

$$
\tilde{Q} = \tilde{Q}_+ \tilde\Pi_+ + \tilde{Q}_- \tilde\Pi_- = (2 + 2 e_1) \tilde\Pi_+ + (2 e_1 + 2 e_2) \tilde\Pi_-.
$$

Because $\tilde\Pi_\pm$ are central, $\mathbb{H} \tilde\Pi_+$ and $\mathbb{H} \tilde\Pi_-$ are two-sided ideals as well: they are the two quaternion halves of the algebra.

## Explicit Zero Divisors

The simplest zero-divisor pair is the idempotent pair $\tilde\Pi_+ \tilde\Pi_- = 0$, with both factors nonzero. A less trivial pair is obtained by taking an element of one half and an element of the other:

$$
\tilde P = e_1 \tilde\Pi_-, \qquad \tilde{R} = (1 + e_2) \tilde\Pi_+.
$$

In developed form,

$$
\tilde P = \tfrac{1}{2} e_1 (1 - j) = \tfrac{1}{2} e_1 - \tfrac{1}{2} j e_1, \qquad \tilde{R} = \tfrac{1}{2}(1 + e_2)(1 + j) = \tfrac{1}{2}(1 + j) + \tfrac{1}{2}(1 + j) e_2.
$$

Since $\tilde\Pi_- \tilde\Pi_+ = 0$ and $e_1 (1 + e_2) = e_1 + e_1 e_2 = e_1 + e_3$ is a quaternion,

$$
\tilde P \tilde{R} = e_1 (1 + e_2) \tilde\Pi_- \tilde\Pi_+ = 0,
$$

while neither $\tilde P$ nor $\tilde{R}$ is zero. The pair therefore exhibits an explicit zero divisor, and it shows the general shape of the zero divisor set: the zero divisors of $\mathbb{H}_{\mathbb{D}}$ are exactly the elements with $\tilde{Q}_+ = 0$ or $\tilde{Q}_- = 0$, that is, the union of the two halves $\mathbb{H} \tilde\Pi_- \cup \mathbb{H} \tilde\Pi_+$. The classification is developed in *Split-Biquaternion Zero Divisors*.

## The Two Quaternion Halves Realised

The isomorphism $\varphi : \mathbb{H}_{\mathbb{D}} \to \mathbb{H} \oplus \mathbb{H}$, $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$, sends the concrete element to

$$
\varphi(\tilde{Q}) = \big(2 + 2 e_1, \; 2 e_1 + 2 e_2 \big).
$$

Multiplication is componentwise, so the concrete element is a unit in $\mathbb{H}_{\mathbb{D}}$ exactly because each of $2 + 2 e_1$ and $2 e_1 + 2 e_2$ is a nonzero quaternion, hence a unit in $\mathbb{H}$; indeed

$$
(2 + 2 e_1)^{-1} = \tfrac{1}{8}(2 - 2 e_1), \qquad (2 e_1 + 2 e_2)^{-1} = \tfrac{1}{8}(-2 e_1 - 2 e_2),
$$

and $\varphi(\tilde{Q}^{-1}) = \tfrac{1}{8}(2 - 2 e_1, -2 e_1 - 2 e_2)$, which agrees with the inverse $\tilde{Q}^{-1} = \tfrac{1}{8} \tilde{Q}^{\natural}$. The two halves are thus not merely an abstract direct sum: on this element they are the two nonzero quaternions whose product-freeness decides invertibility.

## Summary

The split biquaternion algebra $\mathbb{H}_{\mathbb{D}}$ has the real basis $1, e_1, e_2, e_3, j, j e_1, j e_2, j e_3$ and the product formula $\tilde{Q} \tilde{R} = (Q_0 R_0 - (\mathbf{Q}, \mathbf{R})) e_0 + Q_0 \mathbf{R} + R_0 \mathbf{Q} + [\mathbf{Q}, \mathbf{R}]$. On the concrete element

$$
\tilde{Q} = (1 + j) + 2 e_1 + (1 - j) e_2
$$

the four conjugations act as $\tilde{Q}^{\natural} = (1 + j) - 2 e_1 - (1 - j) e_2$, $\bar{\tilde{Q}} = (1 - j) + 2 e_1 + (1 + j) e_2$, $\tilde{Q}^{*} = \overline{\tilde{Q}^{\natural}}$ and $\tilde{Q}^\flat = -\tilde{Q}^{*}$; the four fixed-point subspaces $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ have dimensions $2, 4, 4, 4$ and overlap, so their projections do not sum to the element. The idempotents $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ are central and primitive and give the two minimal left ideals $\mathbb{H} \tilde\Pi_\pm$; the element decomposes as $\tilde{Q} = (2 + 2 e_1) \tilde\Pi_+ + (2 e_1 + 2 e_2) \tilde\Pi_-$ with both components nonzero. An explicit zero-divisor pair is $\tilde P = e_1 \tilde\Pi_-$ and $\tilde{R} = (1 + e_2) \tilde\Pi_+$, with $\tilde P \tilde{R} = 0$. The isomorphism $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-) = (2 + 2 e_1, 2 e_1 + 2 e_2)$ realises the two quaternion halves, and the square $\tilde{Q}^2 = (-4 + 4 e_1) + j(4 + 4 e_1)$ agrees whether computed from the product formula or from the idempotent components.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D} \otimes_{\mathbb{R}} \mathbb{H}$ | Split biquaternion algebra, $\cong \mathbb{H} \oplus \mathbb{H}$ |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis |
| $j$ | Split complex unit, central, $j^2 = +1$ |
| $\tilde\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ | The idempotents, $\tilde\Pi_+ + \tilde\Pi_- = 1$ |
| $\tilde{Q} = A + j B$ | Concrete element, $A, B \in \mathbb{H}$ |
| $\tilde{Q}_\pm = \tilde{Q} \tilde\Pi_\pm$ | Idempotent components in $\mathbb{H}$ |
| ${}^{\natural}, \bar{\cdot}, {}^{*}, {}^{\flat}$ | The four conjugations |
| $\mathbb{D}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}, \mathbb{M}_+, \mathbb{M}_-$ | The four involution fixed-point subspaces |
| $\mathbb{H} \tilde\Pi_\pm$ | The two minimal left ideals, each $\cong \mathbb{H}$ |
| $\varphi(\tilde{Q}) = (\tilde{Q}_+, \tilde{Q}_-)$ | Idempotent-decomposition isomorphism |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the quaternion multiplication table and the scalar-vector product formula.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic biquaternion calculus.
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997), for worked computations in the split biquaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the idempotent basis and the direct-sum structure of Clifford algebras of split signature.
