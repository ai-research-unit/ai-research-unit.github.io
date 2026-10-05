# __The Bilinear Form on the Biquaternion Algebra__

## Introduction

The biquaternion algebra carries two scalar pairings, and this article treats the first of them. The **bilinear form** is

$$
N(\tilde{P}, \tilde{Q}) = \mathrm{Sc}\!\left(\tilde{P}\, \tilde{Q}^{\natural}\right) = \sum_{\mu=0}^{3} P_\mu Q_\mu ,
$$

built on the **natural** conjugation ${}^{\natural}$, which is $\mathbb{C}$-linear, so that the form is $\mathbb{C}$-**bilinear**: scalars may be moved out of either argument. Its diagonal $N(\tilde{Q},\tilde{Q})$ is the biquaternion norm $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ of *Biquaternion Norm and Invertibility*, and the form is the polarisation of that quadratic form.

This is the form the Algebra group does not use: the articles *Biquaternions as a Vector Space over $\mathbb{C}$* and the six subspace articles work with ${}^{\natural}$, without using the norm — its sign, its signature, its definiteness, its Euclidean part. The companion pairings are *The Hermitian Form on the Biquaternion Algebra*, built on the Hermitian conjugation ${}^{*}$, and *The Biquaternion Krein Form and Its Signature*, built on the complex conjugation $\bar{\cdot}$.

## The Form and Its Polarisation

Because ${}^{\natural}$ is $\mathbb{C}$-linear, the pairing

$$
N(\tilde{P}, \tilde{Q}) = \mathrm{Sc}\!\left(\tilde{P}\, \tilde{Q}^{\natural}\right)
$$

is $\mathbb{C}$-**bilinear**, symmetric, and non-degenerate; its diagonal is the biquaternion norm. It is the **polar form** of that norm,

$$
N(\tilde{P}, \tilde{Q}) = \tfrac{1}{2}\left(N(\tilde{P}+\tilde{Q}) - N(\tilde{P}) - N(\tilde{Q})\right),
$$

and it is the $\mathbb{C}$-bilinear pairing built on ${}^{\natural}$, distinguished by the involution that twists it from the $\mathbb{C}$-sesquilinear ones built on ${}^{*}$ (*The Group of Involutions*; *The Hermitian Form on the Biquaternion Algebra*).

The form is **multiplicative** in the following sense: for a quaternion $a \in \mathbb{H}_{\mathbb{B}}$ acting by left multiplication, $N(a\tilde{P}, a\tilde{Q}) = N(a)^2 N(\tilde{P},\tilde{Q})$, and likewise on the right, since $N$ is multiplicative and central. Over $\mathbb{C}$ the form is a non-degenerate complex quadratic form; it has no signature until a real form is chosen, and the signature is read from the real slices below.

## The Restriction to the Six Subspaces

The form restricts to each of the six distinguished real subspaces, and the real signature of the restriction is the quantity the Algebra articles record only as a pointer. With $Q_\mu = q_\mu + i q'_\mu$ and $q_\mu, q'_\mu \in \mathbb{R}$,

| Real subspace | $N$ restricted | Signature |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Q_0^2 = q_0^2 - (q'_0)^2$ | $(1,1)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\sum_k Q_k^2 = \sum_k \left(q_k^2 - (q'_k)^2\right)$ | $(3,3)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\sum_\mu q_\mu^2$ | $(4,0)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $-\sum_\mu (q'_\mu)^2$ | $(0,4)$ |
| $\mathbb{M}_+$ | $q_0^2 - \sum_k (q'_k)^2$ | $(1,3)$ |
| $\mathbb{M}_-$ | $\sum_k q_k^2 - (q'_0)^2$ | $(3,1)$ |

The six rows are the content of the tables in *Biquaternion Norm and Invertibility*, §*The Real Forms and Their Signatures*, where the realification of $N$ on $\mathbb{R}^8$ is also computed: it is the split form of signature $(4,4)$. Four of the six subspaces give a real form on which $N$ is real-valued — the quaternion subspace, the anti-quaternion subspace and the two sectors — and the two that do not are the centre and the vector subspace, on which $N$ is complex.

The **polar form** of the restriction is the corresponding symmetric bilinear form: on the Hermitian subspace

$$
B(\tilde{Q}, \tilde{R}) = q_0 r_0 - (\mathbf{q}', \mathbf{r}'),
$$

and on the anti-Hermitian subspace

$$
B(\tilde{Q}, \tilde{R}) = (\mathbf{q}, \mathbf{r}) - q'_0 r'_0 ,
$$

the two differing by a sign, as their signatures $(1,3)$ and $(3,1)$ indicate.

## The Null Cone

The **null cone** is the zero set of the norm,

$$
\{\tilde{Q} : N(\tilde{Q}) = 0\}.
$$

Over $\mathbb{C}$ it is a complex cone through the origin; on the vector subspace its real dimension is four, and on each of the two sectors its real dimension is three. The cone is the set on which the algebra fails to be a division algebra: a non-zero element is a zero divisor exactly when it is null, so the null cone is the union of the two families of zero divisors classified in *Biquaternion Zero Divisors*. The projective picture of the cone, its link, and the associated quadrics are *Biquaternion Topology* and *Biquaternion Lorentzian and Conformal Geometry*.

## Summary

The bilinear form of the biquaternion algebra is $N(\tilde{P},\tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural}) = \sum_\mu P_\mu Q_\mu$, the polarisation of the biquaternion norm. It is $\mathbb{C}$-bilinear and non-degenerate, and its restriction to each of the six distinguished real subspaces carries the signature that this article records: $(1,1)$ on the centre, $(3,3)$ on the vector subspace, $(4,0)$ on the quaternion subspace, $(0,4)$ on the anti-quaternion subspace, $(1,3)$ on the Hermitian subspace and $(3,1)$ on the anti-Hermitian subspace. Its realification on $\mathbb{R}^8$ is the split form of signature $(4,4)$. Its null cone is the zero-divisor set of the algebra. The metric read from the norm is *Biquaternion Norm and Invertibility*; the sesquilinear companion is *The Hermitian Form on the Biquaternion Algebra*; and the transpose that the form defines on the linear operators is *Association and the Transpose on the Biquaternion Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $N(\tilde{P}, \tilde{Q}) = \mathrm{Sc}(\tilde{P}\tilde{Q}^{\natural}) = \sum_\mu P_\mu Q_\mu$ | The bilinear form; $\mathbb{C}$-bilinear, symmetric, non-degenerate |
| $N(\tilde{Q}) = N(\tilde{Q},\tilde{Q}) = \sum_\mu Q_\mu^2$ | The biquaternion norm, the diagonal of the form |
| $\{\tilde{Q} : N(\tilde{Q}) = 0\}$ | The null cone; the zero-divisor set |
| $(1,1)$, $(3,3)$, $(4,0)$, $(0,4)$, $(1,3)$, $(3,1)$ | The signatures on the six subspaces |

## Further Reading

- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, its polarisation and the real forms with their signatures
- *The Hermitian Form on the Biquaternion Algebra* (`articles_maths/the-hermitian-form-on-the-biquaternion-algebra.md`), for the sesquilinear companion
- *Biquaternions as a Vector Space over $\mathbb{C}$* (`articles_maths/biquaternions-as-a-vector-space-over-c.md`), for the conjugations and the norm as an algebraic operation
- *Biquaternion Relations Between Subspaces* (`articles_maths/biquaternion-relations-between-subspaces.md`), for the six subspaces
- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the null cone as the zero-divisor set
