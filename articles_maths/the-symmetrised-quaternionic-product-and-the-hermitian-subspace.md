
# __The Symmetrised Quaternionic Product and the Hermitian Subspace__

## Introduction

The product of this group is the **general quaternionic bilinear product**

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q , \qquad \tilde P^{\natural} = P_0 - \mathbf P ,
$$

the second of the four general products of the biquaternion algebra $\mathbb{B}$ (*The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Bilinear Product*), whose algebra, left unit and associativity defect are *Introduction to the General Quaternionic Algebra of Biquaternions* and the previous article of the group. Every bilinear product has two halves, its symmetrisation and its antisymmetrisation (*The 12 Products of the Biquaternion Complex Space*); this article reads the symmetric half,

$$
\tilde P \circ \tilde Q = \tfrac12\bigl(\tilde P\star\tilde Q + \tilde Q\star\tilde P\bigr) = \tfrac12\bigl(\tilde P^{\natural}\tilde Q + \tilde Q^{\natural}\tilde P\bigr) ,
$$

the **symmetrised quaternionic product**. It is commutative by construction, and it is the operation that the general theory of a bilinear product feeds into the Jordan and ternary constructions (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*).

The article establishes four things. First, the symmetrised value is always **central**,

$$
\tilde P \circ \tilde Q = \bigl(P_0Q_0 + (\mathbf P,\mathbf Q)\bigr)e_0 ,
$$

because the two cross-product terms are antisymmetric and the two mixed terms cancel in the half-sum; the two summands of the symmetrisation are exchanged by the conjugation ${}^{\natural}$, which is the structural reason for the centrality. Second, the coefficient $\beta(\tilde P,\tilde Q) = P_0Q_0 + (\mathbf P,\mathbf Q)$ is read on each of the six distinguished subspaces, and the value is Hermitian — lies in the Hermitian subspace $\mathbb{M}_+$, indeed in the real line $\mathbb{R}e_0$ — exactly when $\beta$ is real; this holds for every pair drawn from the quaternion subspace, the anti-quaternion subspace, $\mathbb{M}_+$ and $\mathbb{M}_-$, and on the centre and on the vector subspace only when the corresponding coefficient is real, which is not the generic case. Third, the Hermitian subspace is nonetheless the natural home of the symmetrisation, and the reason is a statement of **closure**: the symmetrisation keeps the centre, the quaternion subspace and the Hermitian subspace inside themselves, and no other subspace of the six (*The Six Subspaces and the Four General Products*). Fourth, the symmetrisation is not a Jordan algebra: it fails the Jordan identity, at $\tilde P = \tilde Q = e_3$ and at $e_1$, and with the identity it fails power-associativity; the flexibility and third-power laws hold, because the value is central.

## The Symmetrised Product

**Theorem (the symmetrised value is central).** For all $\tilde P,\tilde Q \in \mathbb{B}$,

$$
\tilde P \circ \tilde Q = \bigl(P_0Q_0 + (\mathbf P,\mathbf Q)\bigr)e_0 .
$$

**Proof.** Write the two summands from the scalar–vector form of the product: the scalar part of $\tilde P^{\natural}\tilde Q$ is $P_0Q_0 + (\mathbf P,\mathbf Q)$ and its vector part is $P_0\mathbf Q - Q_0\mathbf P - \mathbf P\times\mathbf Q$, while the scalar part of $\tilde Q^{\natural}\tilde P$ is the same and its vector part is $Q_0\mathbf P - P_0\mathbf Q - \mathbf Q\times\mathbf P$. In the half-sum the two mixed terms $P_0\mathbf Q - Q_0\mathbf P$ and $Q_0\mathbf P - P_0\mathbf Q$ cancel, and the two cross products cancel against one another by the antisymmetry $\mathbf P\times\mathbf Q = -\mathbf Q\times\mathbf P$; the scalar parts add to $2\beta(\tilde P,\tilde Q)$ and the half converts them to the displayed coefficient. $\square$

**Corollary.** The symmetrisation is commutative, $\tilde P\circ\tilde Q = \tilde Q\circ\tilde P$, and its value lies in the centre $\mathbb{C}e_0$ for every pair. In particular the symmetrisation takes no value outside the central line unless the coefficient is read, and the two halves of $\star$ recover the product,

$$
\tilde P\star\tilde Q = \tilde P\circ\tilde Q + \tfrac12\bigl[\tilde P,\tilde Q\bigr]_{\star} , \qquad \bigl[\tilde P,\tilde Q\bigr]_{\star} = \tilde P^{\natural}\tilde Q - \tilde Q^{\natural}\tilde P .
$$

**Remark (the two summands are exchanged by the conjugation).** The natural conjugation is an anti-automorphism of order two, so $(\tilde P^{\natural}\tilde Q)^{\natural} = \tilde Q^{\natural}\tilde P$: the conjugation exchanges the two summands of the symmetrisation. The average of two quantities exchanged by an involution is fixed by it, and the elements fixed by ${}^{\natural}$ are exactly the central ones; this is the structural reason for the centrality of the corollary, and it also shows why the individual summands are not central while their average is. The same computation is the reason the symmetrisation of the sesquilinear products of the sibling group behaves differently: there the exchanging map carries a conjugate-linear slot.

**Definition.** The **symmetrised quaternionic product** is the commutative operation $\circ$ on $\mathbb{B}$, with $\tilde P\circ\tilde Q = \tfrac12(\tilde P\star\tilde Q + \tilde Q\star\tilde P)$, and the central coefficient is written

$$
\beta(\tilde P,\tilde Q) = P_0Q_0 + (\mathbf P,\mathbf Q) , \qquad \tilde P\circ\tilde Q = \beta(\tilde P,\tilde Q)\,e_0 .
$$

**Remark (the symmetrisation is the polarisation of the square).** The symmetrisation of a bilinear product is the polarisation of its square map: expanding $\tilde P\star\tilde P + \tilde P\star\tilde Q + \tilde Q\star\tilde P + \tilde Q\star\tilde Q = (\tilde P+\tilde Q)\star(\tilde P+\tilde Q)$ and using the bilinearity gives

$$
\tilde P\circ\tilde Q = \tfrac12\Bigl((\tilde P+\tilde Q)\star(\tilde P+\tilde Q) - \tilde P\star\tilde P - \tilde Q\star\tilde Q\Bigr) .
$$

This is the general construction of the symmetrisation, and with the central square of the group it reads

$$
\tilde P\circ\tilde Q = \tfrac12\Bigl(N(\tilde P+\tilde Q) - N(\tilde P) - N(\tilde Q)\Bigr)e_0 ,
$$

so the central coefficient $\beta(\tilde P,\tilde Q)$ is exactly the polarisation of the norm form, $\beta(\tilde P,\tilde Q) = \tfrac12\bigl(N(\tilde P+\tilde Q)-N(\tilde P)-N(\tilde Q)\bigr)$, and the symmetrised product is the bilinear form of the algebra placed on the central line. In coordinates $\beta(\tilde P,\tilde Q) = \sum_{\mu=0}^{3}P_\mu Q_\mu$ is the standard symmetric $\mathbb{C}$-bilinear form of $\mathbb{C}^4$, so it is symmetric and non-degenerate, with the basis $e_0,e_1,e_2,e_3$ orthonormal; the written source calls it the trace form of the general quaternionic bilinear product (*The Six Subspaces and the Four General Products*).

## The Coefficient on the Six Subspaces

The coefficient $\beta$ is a symmetric $\mathbb{C}$-bilinear form on $\mathbb{B}$, and the whole content of the symmetrisation is its reading on the six distinguished subspaces of *Introduction to the Six Subspaces*. Here $A \in \mathbb{C}$, $h$ and $g$ are real quaternions, $a_0,b_0,c_0 \in \mathbb{R}$, and $\mathbf p,\mathbf q,\mathbf r \in \mathbb{R}^3$ are real vectors.

| subspace | elements | $\beta$ | real for |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_0$, $Be_0$ | $AB$ | real only when $AB$ is real |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf P$, $\mathbf Q$ | $(\mathbf P,\mathbf Q)$ | special pairs only |
| $\mathbb{H}_{\mathbb{B}}$ | $h$, $g$ | $h_0g_0+h_1g_1+h_2g_2+h_3g_3$ | every pair |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$, $ig$ | $-(h_0g_0+h_1g_1+h_2g_2+h_3g_3)$ | every pair |
| $\mathbb{M}_+$ | $a_0e_0+i\mathbf p$, $b_0e_0+i\mathbf r$ | $a_0b_0-(\mathbf p,\mathbf r)$ | every pair |
| $\mathbb{M}_-$ | $ib_0e_0+\mathbf q$, $ic_0e_0+\mathbf r$ | $-b_0c_0+(\mathbf q,\mathbf r)$ | every pair |

**Theorem (when the value is Hermitian).** The value $\tilde P\circ\tilde Q = \beta(\tilde P,\tilde Q)e_0$ is Hermitian — that is, it lies in the Hermitian subspace $\mathbb{M}_+$, indeed in the real line $\mathbb{R}e_0$ — exactly when the coefficient $\beta(\tilde P,\tilde Q)$ is real.

**Proof.** An element $\lambda e_0$ lies in $\mathbb{M}_+$ exactly when $\lambda$ is real, by the coordinate condition of *Introduction to the Six Subspaces* §*The Hermitian Subspace*: the Hermitian subspace is the set of elements with real scalar part and purely imaginary vector part, and $\lambda e_0$ has no vector part; and $\mathbb{R}e_0 \subset \mathbb{M}_+$. $\square$

**Corollary (the coefficient is real on four of the six).** For every pair drawn from the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, from the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, from the Hermitian subspace $\mathbb{M}_+$ or from the anti-Hermitian subspace $\mathbb{M}_-$, the coefficient $\beta$ is real, and the symmetrised value is a real multiple of $e_0$. For a pair drawn from the centre the coefficient is $\beta(Ae_0,Be_0) = AB$, a product of two complex numbers, real only when $AB$ is real, which is not the generic case: the pair $A = 1$, $B = i$ has $\beta = i$. For a pair drawn from the vector subspace, where $\beta(\mathbf P,\mathbf Q) = (\mathbf P,\mathbf Q)$, the coefficient is real only when the general plain bilinear form of the pair is real, which is likewise not the generic case: the pair $\mathbf P = e_1$, $\mathbf Q = ie_1$ has $\beta = i$.

**Proof.** The four entries of the table whose fourth column reads "every pair" are immediate: in each the ingredients of $\beta$ are real. The centre and the vector subspace are the two entries whose fourth column is a condition; on the centre $\beta = AB$ is the plain product in $\mathbb{C}$, real for $A = B = 1$ and non-real for $A = 1$, $B = i$, and on the vector subspace $\beta$ is the general plain bilinear form, real for the pair $e_1,e_1$ and non-real for the pair $e_1,ie_1$. $\square$

**Remark (the coefficient is not the point; the closure is).** The corollary shows that a Hermitian value is the common situation and not the distinction: the value is Hermitian on every pair from four of the six subspaces, and on the centre and on the vector subspace it is Hermitian whenever the coefficient happens to be real. What distinguishes the Hermitian subspace is not that the value of a pair from it is Hermitian, but that the symmetrisation **keeps it inside itself**: for $\tilde P,\tilde Q \in \mathbb{M}_+$ the value is a real multiple of $e_0$, which is again an element of $\mathbb{M}_+$. The same is true of the centre and of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, which contains the real line; and it is false of the vector subspace, of $i\mathbb{H}_{\mathbb{B}}$ and of $\mathbb{M}_-$, where the value escapes to the centre. This is the sense in which the Hermitian subspace is the natural home of the symmetrisation, and it is the statement of *The Six Subspaces and the Four General Products* that the symmetrisation of every one of the four general products stays inside exactly the centre, the quaternion subspace and the Hermitian subspace.

**Example.** On $\mathbb{M}_+$, with $\tilde P = a_0e_0+i\mathbf p$ and $\tilde Q = b_0e_0+i\mathbf r$ real, the symmetrised value is $\bigl(a_0b_0-(\mathbf p,\mathbf r)\bigr)e_0$: a real element of the real line, inside $\mathbb{M}_+$. On $\mathbb{M}_-$, with $\tilde P = ib_0e_0+\mathbf q$ and $\tilde Q = ic_0e_0+\mathbf r$, the value is $\bigl(-b_0c_0+(\mathbf q,\mathbf r)\bigr)e_0$: again real, but $\mathbb{M}_-$ has a purely imaginary scalar part and a real vector part, so the value is Hermitian and **not** anti-Hermitian, and it has left the subspace. The sign that produces the two formulas is the same: the real vector part of the anti-Hermitian element enters the coefficient without an imaginary unit, while its imaginary scalar part contributes the negative product.

## The Failure of the Jordan Identity

A commutative algebra is a **Jordan algebra** when it satisfies the Jordan identity; the symmetrisation of an associative algebra always does, and the symmetrisation here does not.

**Theorem (the Jordan identity fails).** The symmetrisation $\circ$ does not satisfy the Jordan identity

$$
\tilde P\circ\bigl(\tilde Q\circ(\tilde P\circ\tilde P)\bigr) = \bigl(\tilde P\circ\tilde Q\bigr)\circ\bigl(\tilde P\circ\tilde P\bigr) .
$$

At $\tilde P = \tilde Q = e_3$ the two sides are $0$ and $e_0$; at $\tilde P = e_1$, $\tilde Q = e_1$ they are $0$ and $e_0$ as well.

**Proof.** Take $\tilde P = \tilde Q = e_3$. The square is $e_3\circ e_3 = \beta(e_3,e_3)e_0 = e_0$, since $\beta(e_3,e_3) = 1$. The left side is $e_3\circ(e_3\circ(e_3\circ e_3)) = e_3\circ(e_3\circ e_0)$, and $e_3\circ e_0 = \beta(e_3,e_0)e_0 = 0$, so it is $0$. The right side is $(e_3\circ e_3)\circ(e_3\circ e_3) = e_0\circ e_0 = \beta(e_0,e_0)e_0 = e_0$. The same evaluation at $e_1$ gives $e_1\circ e_1 = e_0$ and the same two values. $\square$

**Corollary (not power-associative).** The symmetrisation is not power-associative. At $x = e_3$ the fourth power read one way is $x^2\circ x^2 = e_0$ and read the other is $x\circ x^3 = x\circ(x\circ x^2) = e_3\circ(e_3\circ e_0) = 0$; the two readings differ, so the subalgebra generated by $e_3$ is not associative.

**Proof.** The displayed computation is the Jordan identity at $x = y = e_3$ rewritten as $x^2\circ x^2 = x\circ x^3$; power-associativity requires $x^px^q = x^{p+q}$ for all $p,q$, in particular $x^2x^2 = xx^3$, and the two sides are $e_0$ and $0$. $\square$

**Remark (which weaker laws still hold).** The **flexible** law and the **third-power** law hold, and they hold for the same reason: the inner symmetrisation is central, so the two sides of $(\tilde P\circ\tilde Q)\circ\tilde P = \tilde P\circ(\tilde Q\circ\tilde P)$ are both $\beta(\tilde P,\tilde Q)P_0e_0$, and the two sides of $\tilde P\circ(\tilde P\circ\tilde P) = (\tilde P\circ\tilde P)\circ\tilde P$ are both $\beta(\tilde P,\tilde P)P_0e_0$. What fails is the Jordan identity itself, and with it power-associativity. The reason is the centrality of the value: the symmetrisation collapses every product to a multiple of $e_0$, so the two parenthesizations of the fourth power are not forced to agree, and at $e_3$ they are $0$ and $e_0$. This is the exact place at which the symmetrisation of the quaternionic product parts company with the symmetrisation of the associative product, which satisfies the identity because the underlying product is associative.

## The Contrast with the Jordan Product of the Algebra

**The Jordan product of the algebra.** The symmetrisation of the associative multiplication,

$$
\tilde P \bullet \tilde Q = \tfrac12\bigl(\tilde P\tilde Q + \tilde Q\tilde P\bigr) ,
$$

does satisfy the Jordan identity, because it is the symmetrisation of an associative product; this is the general reason special Jordan algebras exist (*Jordan Algebras* §*The Symmetrisation of an Associative Algebra*). Its reading on the six subspaces is *The 12 Products of the Biquaternion Complex Space* and *The 12 Products of the Biquaternion Complex Space*: on the Hermitian subspace it is the Jordan product, and $(\mathbb{M}_+,\bullet) \cong H_2(\mathbb{C}) = J(\mathbb{B})$ is the Hermitian Jordan algebra of degree two; on the quaternion subspace it is the symmetrisation of the real quaternion algebra; and on the Hermitian subspace the two quaternionic symmetrisations, the present one among them, are central and give no Jordan algebra (*The Six Subspaces and the Four General Products*).

**Why the central value cannot be the Jordan product.** The product $\circ$ is the only commutative $\mathbb{C}$-bilinear operation on $\mathbb{B}$ that is built from $\star$ alone and is fixed by the exchange of the two arguments; and a candidate Jordan product of the quaternionic multiplication would have to be a commutative product satisfying the identity. The value of $\circ$ is central for every pair, and the theorem above exhibits the failure of the identity; so no scalar multiple of the central value, and no correction of it by a central term, can serve, the identity being non-linear in the product. The Jordan structure of $\mathbb{B}$ is therefore carried by the symmetrisation of its associative multiplication and not by the symmetrisation of the quaternionic one, and the two operations are genuinely different and not two readings of one: they agree on the centre, where both are the multiplication of $\mathbb{C}$, and part company as soon as a vector part is present, since the value of $\circ$ has no vector part while the value of $\bullet$ does, and the central coefficients carry the polarised norm $(\mathbf P,\mathbf Q)$ with opposite signs. It is the third face of the same fact as the previous two articles: the product $\star$ moves the element-theoretic data of the algebra — the idempotents become trivial, the square-zero set becomes the whole cone, and the Jordan algebra disappears.

## Summary

The symmetrised quaternionic product $\tilde P\circ\tilde Q = \tfrac12(\tilde P^{\natural}\tilde Q + \tilde Q^{\natural}\tilde P)$ is commutative, and its value is the central element $\beta(\tilde P,\tilde Q)e_0$ with $\beta = P_0Q_0+(\mathbf P,\mathbf Q)$, the centrality coming from the conjugation exchanging the two summands. The value is Hermitian exactly when $\beta$ is real, which holds for every pair drawn from the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace or the anti-Hermitian subspace, and on the centre and on the vector subspace only when the coefficient happens to be real, as it is not for the pair $A = 1$, $B = i$ in the centre. What singles out the Hermitian subspace is that the symmetrisation keeps it inside itself, as it does the centre and the quaternion subspace, and no other subspace of the six. The symmetrisation fails the Jordan identity at $e_3$ and at $e_1$, where the two sides are $0$ and $e_0$, and it fails power-associativity; the flexibility and third-power laws hold, because the value is central. The contrast is the Jordan product $\bullet$ of the associative multiplication, which satisfies the identity and gives the algebra its special Jordan structures; the central value of $\circ$ cannot be that Jordan product, and the discrepancy is the third face of the way the product $\star$ displaces the element-theoretic data of $\mathbb{B}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the identity, $e_k^2 = -e_0$ |
| $\tilde P = \sum_\mu P_\mu e_\mu$ | an element and its four complex coordinates |
| $\mathbf P = \sum_{k=1}^{3}P_ke_k$ | the vector part |
| $(\mathbf P,\mathbf Q)$ | the complex bilinear dot product $\sum_k P_kQ_k$ |
| $\mathbf P\times\mathbf Q$ | the complex bilinear cross product |
| ${}^{\natural}$ | the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$ |
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q$ | the general quaternionic bilinear product, the multiplication of this group |
| $\tilde P\circ\tilde Q = \tfrac12(\tilde P\star\tilde Q+\tilde Q\star\tilde P)$ | the symmetrised quaternionic product |
| $\beta(\tilde P,\tilde Q) = P_0Q_0+(\mathbf P,\mathbf Q)$ | its central coefficient |
| $\tilde P\bullet\tilde Q = \tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ | the Jordan product of the associative multiplication |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the centre, the vector, quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan identity, the symmetrisation of an associative algebra and the resulting special Jordan algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for power-associativity, the quadratic representation and the place of the identity among the weaker laws.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the symmetrisation of a non-associative product and the identities it does and does not inherit.
- Pascual Jordan, John von Neumann and Eugene Wigner, "On an algebraic generalization of the quantum mechanical formalism", *Annals of Mathematics* 35 (1934), 29–64, for the Jordan product and the identity that defines the algebras.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for an involution exchanging two summands and fixing their average.
