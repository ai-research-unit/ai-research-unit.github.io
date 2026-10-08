# __The Quaternion Form as a Product on the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication is a form placed on the central line: the value of
$\tilde P\star\tilde Q$ is the central element $B(\tilde P,\tilde Q)e_0$, and the whole content of the
operation is the coefficient $B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$
(*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). This article reads the coefficient
as the **form that the block carries**: it identifies it, computes its Gram matrix and its rank, its
realification and its signature, its invariance under the product and the failure of that invariance, its
restriction to the six distinguished subspaces, and its relation to the Hermitian form $H$ of the algebra.

The form $B$ is the quaternion form named in the catalogue *The 12 Algebraic Structures over the Biquaternion
$\mathbb{C}$ Space*, and it is the general quaternionic bilinear one of the four pairings of *The Four
Pairings of the Biquaternion Algebra*; its diagonal is the norm of *Biquaternion
Norm and Invertibility*, and on the six subspaces its restrictions and their signatures are
*The Six Subspaces under the General Quaternionic Algebra of Biquaternions*, whose table is quoted here and
not recomputed. The article therefore owns the reading of the form **as the form of the product** — the Gram
data, the invariance question and the coincidence with $H$ — and cites the norm article and the six-subspace
article for the form itself. The Hermitian form $H$ is *Biquaternion Norm and Invertibility*; the invariance
question for a symmetric product is *Jordan Algebras*; the matrix reading of the same form is
*The Symmetric Quaternionic Algebra in the Matrix Representations*.

**Conventions.** The operation is $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$ with
$B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$; the norm is $N(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$;
the Hermitian form is $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$; the real basis
of the algebra is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ over $\mathbb{R}$; the six subspaces are
$\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$,
$\mathbb{M}_+$ and $\mathbb{M}_-$.

## The Form Read as a Product

**Definition.** The **quaternion form** of the block is the symmetric $\mathbb{C}$-bilinear form

$$
B(\tilde P,\tilde Q) = P_0Q_0 + (\mathbf P,\mathbf Q), \qquad
(\mathbf P,\mathbf Q) = \sum_{k=1}^{3}P_kQ_k ,
$$

and it is the coefficient of the product, $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$.

**Proposition (the form determines the product and is determined by it).** The product $\star$ and the form
$B$ determine one another: $\tilde P\star\tilde Q=B(\tilde P,\tilde Q)e_0$, and
$B(\tilde P,\tilde Q)=\operatorname{Sc}(\tilde P\star\tilde Q)$. Consequently the structural data of the
block and of the form are the same data.

*Proof.* The two displays are the definition of the product and the reading of the scalar part of a central
value. $\square$

**Remark (the form is the scalar part of the parent product and the norm is its diagonal).** The coefficient
is the scalar part of the general quaternionic product, $B(\tilde P,\tilde Q)=\operatorname{Sc}(\tilde P^{\natural}\tilde Q)$,
and its diagonal is the multiplicative norm, $N(\tilde Q)=B(\tilde Q,\tilde Q)=\operatorname{Sc}(\tilde Q^{\natural}\tilde Q)=\tilde Q\tilde Q^{\natural}$.
The form is therefore not arbitrary on $\mathbb{B}$: it is the trace-form pairing of the quaternion factor,
and its multiplicativity property belongs to $N$ and not to $B$. The distinction is the one the block repeats:
$N$ is multiplicative and takes values whose reality depends on the elements, while $B$ is only bilinear.

## The Gram Matrix and the Rank

**Proposition (the Gram matrix and the rank).** In the basis $e_0,e_1,e_2,e_3$ the Gram matrix of $B$ is the
unit matrix,

$$
G = I_4, \qquad B(e_\mu,e_\nu)=\delta_{\mu\nu},
$$

so $B$ is non-degenerate of rank $4$ over $\mathbb{C}$, and its radical — the set of elements paired to zero
with the whole space — is $\{0\}$. The form is the standard symmetric form of $\mathbb{C}^4$ in the basis,
and its index over $\mathbb{R}$ is computed from the realification.

*Proof.* $B(e_\mu,e_\nu)=\delta_{\mu\nu}$ is the basis table of *Introduction to the Symmetric Quaternionic
Algebra of Biquaternions*, and an invertible Gram matrix is the non-degeneracy of the form. The radical is
computed in *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*. $\square$

**Remark (rank four and the centre of the algebra).** The form has rank equal to the dimension of the whole
space, and its image under the product is the central line, of complex dimension one. The rank of the form is
therefore larger than the dimension of the line on which the product takes its values, and the two numbers
must not be conflated: the form pairs all four complex directions, and the product collapses them onto one.

## The Realification and the Signature

**Proposition (the realified form).** In the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ the
realification of $B$ is the diagonal form

$$
\operatorname{diag}(I_4,-I_4),
$$

of signature $(4,4)$ and index $4$; in the interleaved basis $e_0,ie_0,e_1,ie_1,e_2,ie_2,e_3,ie_3$ it is
$\operatorname{diag}(1,-1,1,-1,1,-1,1,-1)$. The restriction to the quaternion subspace $\mathbb{H}_{\mathbb{B}}$
is positive definite of signature $(4,0)$, and the restriction to the anti-quaternion subspace
$i\mathbb{H}_{\mathbb{B}}$ is negative definite of signature $(0,4)$.

*Proof.* The form is $\mathbb{C}$-bilinear and $i$ is central, so the pairing of a real direction with its
imaginary companion is purely imaginary and drops from the realification, while $B(ie_\mu,ie_\nu)=-B(e_\mu,e_\nu)$;
the two blocks are $+I_4$ and $-I_4$ and the interleaved reading is the same matrix permuted. On
$\mathbb{H}_{\mathbb{B}}$ the form is $\sum_\mu q_\mu^2$ with $q_\mu$ real, positive definite; on
$i\mathbb{H}_{\mathbb{B}}$ it is the negative. The computation is the one of *The Six Subspaces under the
General Quaternionic Algebra of Biquaternions*. $\square$

**Remark (a complex form, read twice over the reals).** The signature $(4,4)$ is that of a complex bilinear
form of rank four on a complex space of dimension four, read as a real form on $\mathbb{R}^8$; the index $4$ is
half the real dimension. The two definite rows are the two halves the realification separates, and their
signatures sum to $(4,4)$. The reader is warned that the complex form is non-degenerate and has no
signature in the real sense until the realification is taken; this is the reason the complex rank and the real
signature are both recorded here.

## The Trace Form and the Absence of a Second Form

**Proposition (the trace form).** The form is the trace pairing of the parent product,

$$
B(\tilde P,\tilde Q) = \operatorname{Sc}\bigl(\tilde P^{\natural}\tilde Q\bigr)
= \tfrac12\operatorname{Tr}\bigl(\tilde P^{\natural}\tilde Q\bigr),
$$

and the trace of the left multiplication is the scalar part of the argument,

$$
\operatorname{Tr}\bigl(L^{\star}_{\tilde A}\bigr) = B(\tilde A,e_0) = A_0 .
$$

*Proof.* The first display is the remark of the first section together with the corpus identity
$\operatorname{Tr}(\tilde P\tilde Q)=2\operatorname{Sc}(\tilde P\tilde Q)$ of *Biquaternion Norm and
Invertibility*. For the second, $L^{\star}_{\tilde A}e_\nu=B(\tilde A,e_\nu)e_0=A_\nu e_0$, so the matrix of
$L^{\star}_{\tilde A}$ in the basis has the entries $A_\nu$ at position $(0,\nu)$ and zero elsewhere; the only
nonzero diagonal entry is the one at $(0,0)$, which is $A_0$. $\square$

**Remark (there is one form and not a family).** The block carries the single form $B$: the trace form, the
coefficient of the product, the polarisation of the norm and the Gram data $I_4$ are four readings of the same
object, and $B$ is the only form the product produces. The invariance of the next section does not select a
smaller family of forms: a symmetric $\mathbb{C}$-bilinear form $\beta$ is invariant under $\star$ exactly when
$\beta(e_0,\tilde R)=0$ for every $\tilde R$, so the invariant forms are the symmetric forms vanishing on the
central line, of complex dimension $6$, and every one of them is degenerate. There is no non-degenerate
symmetric form invariant under the product, and $B$ itself is not invariant. The operator article *The
Multiplication Operators of the Symmetric Quaternionic Algebra* records the adjoint with respect to $B$ and
the groups that preserve it.

## The Invariance, and Its Failure

**Definition.** The form $B$ is **invariant under the product** when

$$
B(\tilde P\star\tilde Q,\tilde R) = B(\tilde P,\tilde Q\star\tilde R)
$$

for all $\tilde P,\tilde Q,\tilde R\in\mathbb{B}$; equivalently when
$B\bigl(B(\tilde P,\tilde Q)e_0,\tilde R\bigr)=B\bigl(\tilde P,B(\tilde Q,\tilde R)e_0\bigr)$.

**Theorem (the form is not invariant).** The form $B$ is not invariant under $\star$. At
$\tilde P=\tilde Q=e_1$ and $\tilde R=e_0$ the two sides are $1$ and $0$:

$$
B(\tilde P\star\tilde Q,\tilde R)=B(e_0,e_0)=1, \qquad
B(\tilde P,\tilde Q\star\tilde R)=B(e_1,0)=0 .
$$

*Proof.* $e_1\star e_1=e_0$ and $e_1\star e_0=0$; the two displayed forms are then $B(e_0,e_0)=1$ and
$B(e_1,0)=0$. $\square$

**Remark (why the failure is forced).** The two sides of the invariance are
$B(\tilde P,\tilde Q)R_0$ and $P_0B(\tilde Q,\tilde R)$, and they agree for all arguments only if the
operation is associative in a way the block does not have. The failure is the same computation as the
non-vanishing associator of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*,
because $B(\tilde P\star\tilde Q,\tilde R)$ is the scalar part of the first bracketing of the associator. A
symmetric form that is invariant under a commutative product and has a unit is the coefficient form of a
Jordan algebra; here there is no unit and the invariance fails, which is the form-theoretic face of the
failure of the Jordan identity (*Jordan Algebras*).

## The Restriction to the Six Subspaces

The restrictions of $B$ to the six distinguished subspaces are the restrictions of the quaternion form
computed in *The Six Subspaces under the General Quaternionic Algebra of Biquaternions*, whose table is
quoted here; the present article adds only their reading through the product. Here $A,B\in\mathbb{C}$, $h,g$
are real quaternions, $a_0,b_0\in\mathbb{R}$ and $\mathbf p,\mathbf q\in\mathbb{R}^3$ are real vectors.

| subspace | elements | $B$ | dimension over $\mathbb{R}$ | signature | isotropic elements |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_0$, $Be_0$ | $AB$ | $2$ | $(1,1)$ | none (complex form) |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbf P$, $\mathbf Q$ | $(\mathbf P,\mathbf Q)$ | $6$ | $(3,3)$ | the pure zero divisors |
| $\mathbb{H}_{\mathbb{B}}$ | $h$, $g$ | $h_0g_0+\cdots+h_3g_3$ | $4$ | $(4,0)$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$, $ig$ | $-(h_0g_0+\cdots+h_3g_3)$ | $4$ | $(0,4)$ | none |
| $\mathbb{M}_+$ | $a_0e_0+i\mathbf p$, $b_0e_0+i\mathbf q$ | $a_0b_0-(\mathbf p,\mathbf q)$ | $4$ | $(1,3)$ | the elements $a_0e_0+i\mathbf p$ with $a_0^2=(\mathbf p,\mathbf p)$ |
| $\mathbb{M}_-$ | $ia_0e_0+\mathbf p$, $ib_0e_0+\mathbf q$ | $(\mathbf p,\mathbf q)-a_0b_0$ | $4$ | $(3,1)$ | the elements $\mathbf p+ia_0e_0$ with $(\mathbf p,\mathbf p)=a_0^2$ |

**Remark (the product on each restriction).** On every one of the six the product of two elements is a
multiple of $e_0$ read through the displayed coefficient, and the square of an element is the value of the
restricted diagonal. The two definite rows have no isotropic element; the centre has none for the complex
form although its realification has the two real isotropic lines; the vector subspace carries the pure
zero-divisor cone; and the two Hermitian subspaces carry their real light cones. The product has no unit on
any of the six, since it has none on the whole algebra.

## The Coincidence with the Hermitian Form on the Real Part

**Proposition (the coincidence on the real elements).** On two elements with real coefficients, drawn from
the quaternion subspace, the form $B$ coincides with the Hermitian form of *Biquaternion Norm and
Invertibility*,

$$
\tilde P,\tilde Q\in\mathbb{H}_{\mathbb{B}} \quad\Longrightarrow\quad
B(\tilde P,\tilde Q) = H(\tilde P,\tilde Q).
$$

For general complex elements the two differ: writing
$\tilde P=\tilde P'+i\tilde P''$ and $\tilde Q=\tilde Q'+i\tilde Q''$ with $\tilde P',\tilde P'',\tilde Q',\tilde Q''$ in
$\mathbb{H}_{\mathbb{B}}$, the real part of $B$ is
$\operatorname{Re}B(\tilde P,\tilde Q)=B(\tilde P',\tilde Q')-B(\tilde P'',\tilde Q'')$, which is $H$ on the real
block and $-H$ on the imaginary block, the two cross blocks being purely imaginary. Taking $\tilde P=e_0$ and
$\tilde Q=ie_0$ exhibits the difference of the two forms.

*Proof.* On real coefficients the conjugation acts trivially, $\overline{Q_0}=Q_0$ and
$\overline{\mathbf Q}=\mathbf Q$, so $H(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)=B(\tilde P,\tilde Q)$.
For $\tilde P=e_0$, $\tilde Q=ie_0$ one has $B=i$ and $H=1\cdot\overline{i}= -i$, which differ. $\square$

**Remark (the collapse with the other central operation on the real part).** The coincidence is the form-level
statement that $\mathrm{SQA}=\mathrm{SPS}$ on the real part, which is one of the two collapses of the twelve
to ten recorded in *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*. The symmetric part
of the plain sesquilinear product has the coefficient $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$,
which is $B$ precisely when the coefficients are real; over $\mathbb{C}$ the two operations differ, and
$B$ is the $\mathbb{C}$-bilinear conjugate of $H$ in the second slot. The block accordingly reads the form
$B$ as the plain form of the operation, and refers to the norm article for the Hermitian form and its
positivity.

## Summary

The form carried by the symmetric quaternionic multiplication is the quaternion form
$B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$, the coefficient of the product and the scalar part of the
parent product $\tilde P^{\natural}\tilde Q$. Its Gram matrix in the basis is $I_4$, so it has rank $4$ over
$\mathbb{C}$ and its radical is trivial; its realification is $\operatorname{diag}(I_4,-I_4)$ of signature
$(4,4)$ and index $4$; its restrictions to the quaternion and anti-quaternion subspaces are the two definite
rows of signatures $(4,0)$ and $(0,4)$; its restrictions to the other four subspaces have signatures
$(1,1)$, $(3,3)$, $(1,3)$ and $(3,1)$ and carry the isotropic elements recorded in the table. The form is the
trace form, $B=\operatorname{Sc}(\tilde P^{\natural}\tilde Q)=\tfrac12\operatorname{Tr}(\tilde P^{\natural}\tilde Q)$,
and the trace of a left multiplication is the scalar part, $\operatorname{Tr}(L^{\star}_{\tilde A})=A_0$. The
form is **not** invariant under the product, the two sides of $B(\tilde P\star\tilde Q,\tilde R)=B(\tilde P,\tilde Q\star\tilde R)$
being $1$ and $0$ at $e_1,e_1,e_0$, which is the form-theoretic face of the failure of the Jordan identity.
On the real elements the form coincides with the Hermitian form $H$, which is the form-level statement of the
collapse $\mathrm{SQA}=\mathrm{SPS}$ on the real part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B(\tilde P,\tilde Q)=P_0Q_0+(\mathbf P,\mathbf Q)$ | the quaternion form of the block, the coefficient of the product |
| $N(\tilde Q)=B(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^2$ | the norm form, the diagonal of $B$ |
| $H(\tilde P,\tilde Q)=P_0\overline{Q_0}+(\mathbf P,\overline{\mathbf Q})$ | the Hermitian form of $\mathbb{B}$ |
| $G=I_4$ | the Gram matrix of $B$ in the basis $e_0,e_1,e_2,e_3$ |
| $\operatorname{diag}(I_4,-I_4)$, signature $(4,4)$ | the realification of $B$ |
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the six signatures of the restrictions to the six subspaces |
| $L^{\star}_{\tilde A}$, $\operatorname{Tr}(L^{\star}_{\tilde A})=A_0$ | the left multiplication and its trace |
| $B(\tilde P\star\tilde Q,\tilde R)=B(\tilde P,\tilde Q\star\tilde R)$ | the invariance that fails |

## Further Reading

- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the quaternion form among the four pairings
- *Comparison Between the Four Biquaternion Products* (`articles_maths/comparison-between-the-four-biquaternion-products.md`), for the quaternion form beside the other three coefficients
- *Biquaternion Norm and Invertibility* (`articles_maths/biquaternion-norm-and-invertibility.md`), for the norm, the polarisation and the Hermitian form
- *The Six Subspaces under the General Quaternionic Algebra of Biquaternions* (`articles_maths/the-six-subspaces-under-the-general-quaternionic-algebra-of-biquaternions.md`), for the restriction Gram matrices and the signatures
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the radical and the isotropic elements
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the adjoint with respect to $B$ and the groups preserving it
