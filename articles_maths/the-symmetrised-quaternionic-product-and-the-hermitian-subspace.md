
# __The Symmetrised Quaternionic Product and the Hermitian Subspace__

## Introduction

The product of this group is the **general quaternionic bilinear product**

$$
\tilde Q_1 \star \tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2 , \qquad \tilde Q_1^{\natural} = Q_{1t} - \vec Q_1 ,
$$

the second of the four general products of the biquaternion algebra $\mathbb{B}$ (*The Four General Products and Their Relations over the Biquaternion Algebra* §*The General Quaternionic Bilinear Product*), whose algebra, left unit and associativity defect are *Introduction to the General Quaternionic Algebra* and *The Associator and the Ternary Product of the Quaternionic Product*. Every bilinear product has two halves, its symmetrisation and its antisymmetrisation (*Symmetric and Antisymmetric Decomposition of the Four General Products*); this article reads the symmetric half,

$$
\tilde Q_1 \bullet \tilde Q_2 = \tfrac12\bigl(\tilde Q_1\star\tilde Q_2 + \tilde Q_2\star\tilde Q_1\bigr) = \tfrac12\bigl(\tilde Q_1^{\natural}\tilde Q_2 + \tilde Q_2^{\natural}\tilde Q_1\bigr) ,
$$

the **symmetrised quaternionic product**. It is commutative by construction, and it is the operation that the general theory of a bilinear product feeds into the Jordan and ternary constructions (*The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*).

**Notation.** The symmetrisation is written with the bare bullet $\tilde Q_1\bullet\tilde Q_2$, as in the symmetric quaternionic block (*The Specificities of the Symmetric Quaternionic Algebra*); the Jordan product $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ of the associative multiplication, read in the last section, is written in full and carries no bullet, and the circle $\circ$ is kept for the composition of maps.

The article establishes four things. First, the symmetrised value is always **central**,

$$
\tilde Q_1 \bullet \tilde Q_2 = \bigl(Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2)\bigr)e_t ,
$$

because the two cross-product terms are antisymmetric and the two mixed terms cancel in the half-sum; the two summands of the symmetrisation are exchanged by the conjugation ${}^{\natural}$, which is the structural reason for the centrality. Second, the coefficient $\beta(\tilde Q_1,\tilde Q_2) = Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2)$ is read on each of the remarkable subspaces, and the value is Hermitian — lies in the Hermitian subspace $\mathbb{M}_+$, indeed in the real line $\mathbb{R}e_t$ — exactly when $\beta$ is real; this holds for every pair drawn from the quaternion subspace, the anti-quaternion subspace, $\mathbb{M}_+$ and $\mathbb{M}_-$, and on the centre and on the vector subspace only when the corresponding coefficient is real, which is not the generic case. Third, the Hermitian subspace is nonetheless the natural home of the symmetrisation, and the reason is a statement of **closure**: the symmetrisation keeps the centre, the quaternion subspace and the Hermitian subspace inside themselves, and no other subspace of the remarkable subspaces (*Remarkable Subspaces and the Four General Products, Forms and Norms*). Fourth, the symmetrisation is not a Jordan algebra: it fails the Jordan identity, at $\tilde Q_1 = \tilde Q_2 = \vec e_z$ and at $\vec e_x$, and with the identity it fails power-associativity; the flexibility and third-power laws hold, because the value is central.

## The Symmetrised Product

**Theorem (the symmetrised value is central).** For all $\tilde Q_1,\tilde Q_2 \in \mathbb{B}$,

$$
\boxed{\; \tilde Q_1 \bullet \tilde Q_2 = \bigl(Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2)\bigr)e_t \;}.
$$

**Proof.** Write the two summands from the scalar–vector form of the product: the scalar part of $\tilde Q_1^{\natural}\tilde Q_2$ is $Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2)$ and its vector part is $Q_{1t}\vec Q_2 - Q_{2t}\vec Q_1 - \vec Q_1\times\vec Q_2$, while the scalar part of $\tilde Q_2^{\natural}\tilde Q_1$ is the same and its vector part is $Q_{2t}\vec Q_1 - Q_{1t}\vec Q_2 - \vec Q_2\times\vec Q_1$. In the half-sum the two mixed terms $Q_{1t}\vec Q_2 - Q_{2t}\vec Q_1$ and $Q_{2t}\vec Q_1 - Q_{1t}\vec Q_2$ cancel, and the two cross products cancel against one another by the antisymmetry $\vec Q_1\times\vec Q_2 = -\vec Q_2\times\vec Q_1$; the scalar parts add to $2\beta(\tilde Q_1,\tilde Q_2)$ and the half converts them to the displayed coefficient.

**Corollary.** The symmetrisation is commutative, $\tilde Q_1\bullet\tilde Q_2 = \tilde Q_2\bullet\tilde Q_1$, and its value lies in the centre $\mathbb{C}e_t$ for every pair. In particular the symmetrisation takes no value outside the central line unless the coefficient is read, and the two halves of $\star$ recover the product,

$$
\boxed{\; \tilde Q_1\star\tilde Q_2 = \tilde Q_1\bullet\tilde Q_2 + \tfrac12\bigl[\tilde Q_1,\tilde Q_2\bigr]_{\star} , \qquad \bigl[\tilde Q_1,\tilde Q_2\bigr]_{\star} = \tilde Q_1^{\natural}\tilde Q_2 - \tilde Q_2^{\natural}\tilde Q_1 \;}.
$$

**Remark (the two summands are exchanged by the conjugation).** The natural conjugation is an anti-automorphism of order two, so $(\tilde Q_1^{\natural}\tilde Q_2)^{\natural} = \tilde Q_2^{\natural}\tilde Q_1$: the conjugation exchanges the two summands of the symmetrisation. The average of two quantities exchanged by an involution is fixed by it, and the elements fixed by ${}^{\natural}$ are exactly the central ones; this is the structural reason for the centrality of the corollary, and it also shows why the individual summands are not central while their average is. The same computation is the reason the symmetrisation of the sesquilinear products of the sibling group behaves differently: there the exchanging map carries a conjugate-linear slot.

**Definition.** The **symmetrised quaternionic product** is the commutative operation $\bullet$ on $\mathbb{B}$, with $\tilde Q_1\bullet\tilde Q_2 = \tfrac12(\tilde Q_1\star\tilde Q_2 + \tilde Q_2\star\tilde Q_1)$, and the central coefficient is written

$$
\beta(\tilde Q_1,\tilde Q_2) = Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2) , \qquad \tilde Q_1\bullet\tilde Q_2 = \beta(\tilde Q_1,\tilde Q_2)\,e_t .
$$

**Remark (the symmetrisation is the polarisation of the square).** The symmetrisation of a bilinear product is the polarisation of its square map: expanding $\tilde Q_1\star\tilde Q_1 + \tilde Q_1\star\tilde Q_2 + \tilde Q_2\star\tilde Q_1 + \tilde Q_2\star\tilde Q_2 = (\tilde Q_1+\tilde Q_2)\star(\tilde Q_1+\tilde Q_2)$ and using the bilinearity gives

$$
\tilde Q_1\bullet\tilde Q_2 = \tfrac12\Bigl((\tilde Q_1+\tilde Q_2)\star(\tilde Q_1+\tilde Q_2) - \tilde Q_1\star\tilde Q_1 - \tilde Q_2\star\tilde Q_2\Bigr) .
$$

This is the general construction of the symmetrisation, and with the central square of the group it reads

$$
\boxed{\; \tilde Q_1\bullet\tilde Q_2 = \tfrac12\Bigl(\langle\tilde Q_1+\tilde Q_2\rangle_{\natural} - \langle\tilde Q_1\rangle_{\natural} - \langle\tilde Q_2\rangle_{\natural}\Bigr)e_t \;},
$$

so the central coefficient $\beta(\tilde Q_1,\tilde Q_2)$ is exactly the polarisation of the norm form, $\beta(\tilde Q_1,\tilde Q_2) = \tfrac12\bigl(\langle\tilde Q_1+\tilde Q_2\rangle_{\natural}-\langle\tilde Q_1\rangle_{\natural}-\langle\tilde Q_2\rangle_{\natural}\bigr)$, and the symmetrised product is the bilinear form of the algebra placed on the central line. In coordinates $\beta(\tilde Q_1,\tilde Q_2) = \sum_{\mu\in\{t,x,y,z\}}Q_{1,\mu} Q_{2,\mu}$ is the standard symmetric $\mathbb{C}$-bilinear form of $\mathbb{C}^4$, so it is symmetric and non-degenerate, with the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ orthonormal; the written source calls it the trace form of the general quaternionic bilinear product (*Remarkable Subspaces and the Four General Products, Forms and Norms*). The norm whose polarisation this is, with its multiplicativity and its one-sided equations, is *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Polarisation*; the symmetrisation is read there as the quadratic form and here as the operation.

## The Coefficient on the Remarkable Subspaces

The coefficient $\beta$ is a symmetric $\mathbb{C}$-bilinear form on $\mathbb{B}$, and the whole content of the symmetrisation is its reading on the remarkable subspaces of *The Six Subspaces*. Here $A \in \mathbb{C}$, $h$ and $g$ are real quaternions, $a_t,b_t,c_t \in \mathbb{R}$, and $\vec p,\vec q,\vec r \in \mathbb{R}^3$ are real vectors.

| subspace | elements | $\beta$ | real for |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_t$, $Be_t$ | $AB$ | real only when $AB$ is real |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec Q_1$, $\vec Q_2$ | $(\vec Q_1,\vec Q_2)$ | special pairs only |
| $\mathbb{H}_{\mathbb{B}}$ | $h$, $g$ | $h_tg_t+h_xg_x+h_yg_y+h_zg_z$ | every pair |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$, $ig$ | $-(h_tg_t+h_xg_x+h_yg_y+h_zg_z)$ | every pair |
| $\mathbb{M}_+$ | $a_te_t+i\vec p$, $b_te_t+i\vec r$ | $a_tb_t-(\vec p,\vec r)$ | every pair |
| $\mathbb{M}_-$ | $ib_te_t+\vec q$, $ic_te_t+\vec r$ | $-b_tc_t+(\vec q,\vec r)$ | every pair |

**Theorem (when the value is Hermitian).** The value $\tilde Q_1\bullet\tilde Q_2 = \beta(\tilde Q_1,\tilde Q_2)e_t$ is Hermitian — that is, it lies in the Hermitian subspace $\mathbb{M}_+$, indeed in the real line $\mathbb{R}e_t$ — exactly when the coefficient $\beta(\tilde Q_1,\tilde Q_2)$ is real.

**Proof.** An element $\lambda e_t$ lies in $\mathbb{M}_+$ exactly when $\lambda$ is real, by the coordinate condition of *The Six Subspaces* §*The Hermitian Subspace*: the Hermitian subspace is the set of elements with real scalar part and purely imaginary vector part, and $\lambda e_t$ has no vector part; and $\mathbb{R}e_t \subset \mathbb{M}_+$.

**Corollary (the coefficient is real on four of the remarkable subspaces).** For every pair drawn from the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, from the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, from the Hermitian subspace $\mathbb{M}_+$ or from the anti-Hermitian subspace $\mathbb{M}_-$, the coefficient $\beta$ is real, and the symmetrised value is a real multiple of $e_t$. For a pair drawn from the centre the coefficient is $\beta(Ae_t,Be_t) = AB$, a product of two complex numbers, real only when $AB$ is real, which is not the generic case: the pair $A = 1$, $B = i$ has $\beta = i$. For a pair drawn from the vector subspace, where $\beta(\vec Q_1,\vec Q_2) = (\vec Q_1,\vec Q_2)$, the coefficient is real only when the general plain bilinear form of the pair is real, which is likewise not the generic case: the pair $\vec Q_1 = \vec e_x$, $\vec Q_2 = i\vec e_x$ has $\beta = i$.

**Proof.** The four entries of the table whose fourth column reads "every pair" are immediate: in each the ingredients of $\beta$ are real. The centre and the vector subspace are the two entries whose fourth column is a condition; on the centre $\beta = AB$ is the plain product in $\mathbb{C}$, real for $A = B = 1$ and non-real for $A = 1$, $B = i$, and on the vector subspace $\beta$ is the general plain bilinear form, real for the pair $\vec e_x,\vec e_x$ and non-real for the pair $\vec e_x,i\vec e_x$.

**Remark (the coefficient is not the point; the closure is).** The corollary shows that a Hermitian value is the common situation and not the distinction: the value is Hermitian on every pair from four of the remarkable subspaces, and on the centre and on the vector subspace it is Hermitian whenever the coefficient happens to be real. What distinguishes the Hermitian subspace is not that the value of a pair from it is Hermitian, but that the symmetrisation **keeps it inside itself**: for $\tilde Q_1,\tilde Q_2 \in \mathbb{M}_+$ the value is a real multiple of $e_t$, which is again an element of $\mathbb{M}_+$. The same is true of the centre and of the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, which contains the real line; and it is false of the vector subspace, of $i\mathbb{H}_{\mathbb{B}}$ and of $\mathbb{M}_-$, where the value escapes to the centre. This is the sense in which the Hermitian subspace is the natural home of the symmetrisation, and it is the statement of *Remarkable Subspaces and the Four General Products, Forms and Norms* that the symmetrisation of every one of the four general products stays inside exactly the centre, the quaternion subspace and the Hermitian subspace.

**Example.** On $\mathbb{M}_+$, with $\tilde Q_1 = a_te_t+i\vec p$ and $\tilde Q_2 = b_te_t+i\vec r$ real, the symmetrised value is $\bigl(a_tb_t-(\vec p,\vec r)\bigr)e_t$: a real element of the real line, inside $\mathbb{M}_+$. On $\mathbb{M}_-$, with $\tilde Q_1 = ib_te_t+\vec q$ and $\tilde Q_2 = ic_te_t+\vec r$, the value is $\bigl(-b_tc_t+(\vec q,\vec r)\bigr)e_t$: again real, but $\mathbb{M}_-$ has a purely imaginary scalar part and a real vector part, so the value is Hermitian and **not** anti-Hermitian, and it has left the subspace. The sign that produces the two formulas is the same: the real vector part of the anti-Hermitian element enters the coefficient without an imaginary unit, while its imaginary scalar part contributes the negative product.

## The Failure of the Jordan Identity

A commutative algebra is a **Jordan algebra** when it satisfies the Jordan identity; the symmetrisation of an associative algebra always does, and the symmetrisation here does not.

**Theorem (the Jordan identity fails).** The symmetrisation $\bullet$ does not satisfy the Jordan identity

$$
\tilde Q_1\bullet\bigl(\tilde Q_2\bullet(\tilde Q_1\bullet\tilde Q_1)\bigr) = \bigl(\tilde Q_1\bullet\tilde Q_2\bigr)\bullet\bigl(\tilde Q_1\bullet\tilde Q_1\bigr) .
$$

At $\tilde Q_1 = \tilde Q_2 = \vec e_z$ the two sides are $0$ and $e_t$; at $\tilde Q_1 = \vec e_x$, $\tilde Q_2 = \vec e_x$ they are $0$ and $e_t$ as well.

**Proof.** Take $\tilde Q_1 = \tilde Q_2 = \vec e_z$. The square is $\vec e_z\bullet \vec e_z = \beta(\vec e_z,\vec e_z)e_t = e_t$, since $\beta(\vec e_z,\vec e_z) = 1$. The left side is $\vec e_z\bullet(\vec e_z\bullet(\vec e_z\bullet \vec e_z)) = \vec e_z\bullet(\vec e_z\bullet e_t)$, and $\vec e_z\bullet e_t = \beta(\vec e_z,e_t)e_t = 0$, so it is $0$. The right side is $(\vec e_z\bullet \vec e_z)\bullet(\vec e_z\bullet \vec e_z) = e_t\bullet e_t = \beta(e_t,e_t)e_t = e_t$. The same evaluation at $\vec e_x$ gives $\vec e_x\bullet \vec e_x = e_t$ and the same two values.

**Corollary (not power-associative).** The symmetrisation is not power-associative. At $x = \vec e_z$ the fourth power read one way is $x^2\bullet x^2 = e_t$ and read the other is $x\bullet x^3 = x\bullet(x\bullet x^2) = \vec e_z\bullet(\vec e_z\bullet e_t) = 0$; the two readings differ, so the subalgebra generated by $\vec e_z$ is not associative.

**Proof.** The displayed computation is the Jordan identity at $x = y = \vec e_z$ rewritten as $x^2\bullet x^2 = x\bullet x^3$; power-associativity requires $x^px^q = x^{p+q}$ for all $p,q$, in particular $x^2x^2 = xx^3$, and the two sides are $e_t$ and $0$.

**Remark (which weaker laws still hold).** The **flexible** law and the **third-power** law hold, and they hold for the same reason: the inner symmetrisation is central, so the two sides of $(\tilde Q_1\bullet\tilde Q_2)\bullet\tilde Q_1 = \tilde Q_1\bullet(\tilde Q_2\bullet\tilde Q_1)$ are both $\beta(\tilde Q_1,\tilde Q_2)Q_{1t}e_t$, and the two sides of $\tilde Q_1\bullet(\tilde Q_1\bullet\tilde Q_1) = (\tilde Q_1\bullet\tilde Q_1)\bullet\tilde Q_1$ are both $\beta(\tilde Q_1,\tilde Q_1)Q_{1t}e_t$. What fails is the Jordan identity itself, and with it power-associativity. The reason is the centrality of the value: the symmetrisation collapses every product to a multiple of $e_t$, so the two parenthesizations of the fourth power are not forced to agree, and at $\vec e_z$ they are $0$ and $e_t$. This is the exact place at which the symmetrisation of the quaternionic product parts company with the symmetrisation of the associative product, which satisfies the identity because the underlying product is associative.

## The Contrast with the Jordan Product of the Algebra

**The Jordan product of the algebra.** The symmetrisation of the associative multiplication,

$$
\tfrac12\bigl(\tilde Q_1\tilde Q_2 + \tilde Q_2\tilde Q_1\bigr) ,
$$

does satisfy the Jordan identity, because it is the symmetrisation of an associative product; this is the general reason special Jordan algebras exist (*Jordan Algebras* §*The Symmetrisation of an Associative Algebra*). Its reading on the remarkable subspaces is *Symmetric and Antisymmetric Decomposition of the Four General Products*: on the Hermitian subspace it is the Jordan product, and $H_2(\mathbb{C}) = J(\mathbb{B})$, the Hermitian Jordan algebra of degree two, is its algebra there; on the quaternion subspace it is the symmetrisation of the real quaternion algebra; and on the Hermitian subspace the two quaternionic symmetrisations, the present one among them, are central and give no Jordan algebra (*Remarkable Subspaces and the Four General Products, Forms and Norms*).

**Why the central value cannot be the Jordan product.** The product $\bullet$ is the only commutative $\mathbb{C}$-bilinear operation on $\mathbb{B}$ that is built from $\star$ alone and is fixed by the exchange of the two arguments; and a candidate Jordan product of the quaternionic multiplication would have to be a commutative product satisfying the identity. The value of $\bullet$ is central for every pair, and the theorem above exhibits the failure of the identity; so no scalar multiple of the central value, and no correction of it by a central term, can serve, the identity being non-linear in the product. The Jordan structure of $\mathbb{B}$ is therefore carried by the symmetrisation of its associative multiplication and not by the symmetrisation of the quaternionic one, and the two operations are genuinely different and not two readings of one: they agree on the centre, where both are the multiplication of $\mathbb{C}$, and part company as soon as a vector part is present, since the value of $\bullet$ has no vector part while the value of the Jordan product of the associative multiplication does, and the central coefficients carry the polarised norm $(\vec Q_1,\vec Q_2)$ with opposite signs. It is the third face of the same fact as the previous two articles: the product $\star$ moves the element-theoretic data of the algebra — the idempotents become trivial, the square-zero set becomes the whole cone, and the Jordan algebra disappears.

## Summary

The symmetrised quaternionic product $\tilde Q_1\bullet\tilde Q_2 = \tfrac12(\tilde Q_1^{\natural}\tilde Q_2 + \tilde Q_2^{\natural}\tilde Q_1)$ is commutative, and its value is the central element $\beta(\tilde Q_1,\tilde Q_2)e_t$ with $\beta = Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$, the centrality coming from the conjugation exchanging the two summands. The value is Hermitian exactly when $\beta$ is real, which holds for every pair drawn from the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace or the anti-Hermitian subspace, and on the centre and on the vector subspace only when the coefficient happens to be real, as it is not for the pair $A = 1$, $B = i$ in the centre. What singles out the Hermitian subspace is that the symmetrisation keeps it inside itself, as it does the centre and the quaternion subspace, and no other subspace of the remarkable subspaces. The symmetrisation fails the Jordan identity at $\vec e_z$ and at $\vec e_x$, where the two sides are $0$ and $e_t$, and it fails power-associativity; the flexibility and third-power laws hold, because the value is central. The contrast is the Jordan product $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ of the associative multiplication, which satisfies the identity and gives the algebra its special Jordan structures; the central value of $\bullet$ cannot be that Jordan product, and the discrepancy is the third face of the way the product $\star$ displaces the element-theoretic data of $\mathbb{B}$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, $e_t$ the identity, $\vec e_k^2 = -e_t$ |
| $\tilde Q_1 = \sum_\mu Q_{1,\mu} e_\mu$ | an element and its four complex coordinates |
| $\vec Q_1 = \sum_{k=1}^{3}Q_{1,k}\vec e_k$ | the vector part |
| $(\vec Q_1,\vec Q_2)$ | the complex bilinear dot product $\sum_k Q_{1,k}Q_{2,k}$ |
| $\vec Q_1\times\vec Q_2$ | the complex bilinear cross product |
| ${}^{\natural}$ | the natural conjugation $\tilde Q_1^{\natural} = Q_{1t} - \vec Q_1$ |
| $\tilde Q_1\star\tilde Q_2 = \tilde Q_1^{\natural}\tilde Q_2$ | the general quaternionic bilinear product, the multiplication of this group |
| $\tilde Q_1\bullet\tilde Q_2 = \tfrac12(\tilde Q_1\star\tilde Q_2+\tilde Q_2\star\tilde Q_1)$ | the symmetrised quaternionic product |
| $\beta(\tilde Q_1,\tilde Q_2) = Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | its central coefficient |
| $\tfrac12(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1)$ | the Jordan product of the associative multiplication |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the centre, the vector, quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces |

## Further Reading

- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the Jordan identity, the symmetrisation of an associative algebra and the resulting special Jordan algebras.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for power-associativity, the quadratic representation and the place of the identity among the weaker laws.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the symmetrisation of a non-associative product and the identities it does and does not inherit.
- Pascual Jordan, John von Neumann and Eugene Wigner, "On an algebraic generalization of the quantum mechanical formalism", *Annals of Mathematics* 35 (1934), 29–64, for the Jordan product and the identity that defines the algebras.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for an involution exchanging two summands and fixing their average.
