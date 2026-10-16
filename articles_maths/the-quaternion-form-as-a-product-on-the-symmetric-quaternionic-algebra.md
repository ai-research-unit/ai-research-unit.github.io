# __The Quaternion Form as a Product on the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication is a form placed on the central line: the value of
$\tilde P\star\tilde Q$ is the central element $\langle\tilde P,\tilde Q\rangle_{\natural}e_0$, and the whole content of the
operation is the coefficient $\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q)$
(*Introduction to the Symmetric Quaternionic Algebra*). This article reads the coefficient
as the **form that the block carries**: it identifies it, computes its Gram matrix and its rank, its
realification and its signature, its invariance under the product and the failure of that invariance, its
restriction to the remarkable subspaces, and its relation to the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ of the algebra.

The form $\langle\cdot,\cdot\rangle_{\natural}$ is the quaternion form named in the catalogue *The 12 Products of the Biquaternioid Complex Space*, and it is the general quaternionic bilinear one of the four pairings of *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; its diagonal is the norm of *Norm and Invertibility in the General Quaternionic Algebra*, and on the remarkable subspaces its restrictions and their signatures are
*Remarkable Subspaces under the General Quaternionic Algebra*, whose table is quoted here and
not recomputed. The article therefore owns the reading of the form **as the form of the product** — the Gram
data, the invariance question and the coincidence with $\langle\cdot,\cdot\rangle_{*}$ — and cites the norm article and the remarkable-subspace
article for the form itself. The Hermitian form $\langle\cdot,\cdot\rangle_{*}$ is *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space*; the invariance
question for a symmetric product is *Jordan Algebras*; the matrix reading of the same form is
*Introduction to the Symmetric Quaternionic Algebra*.

**Conventions.** The operation is $\tilde P\star\tilde Q=\langle\tilde P,\tilde Q\rangle_{\natural}e_0$ with
$\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q)$; the norm is $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$;
the Hermitian form is $\langle\tilde P,\tilde Q\rangle_{*}=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$; the real basis
of the algebra is $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ over $\mathbb{R}$; the remarkable subspaces are
$\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$,
$\mathbb{M}_+$ and $\mathbb{M}_-$.

## The Form Read as a Product

**Definition.** The **quaternion form** of the block is the symmetric $\mathbb{C}$-bilinear form

$$
\langle\tilde P,\tilde Q\rangle_{\natural} = P_0Q_0 + (\vec P,\vec Q), \qquad
(\vec P,\vec Q) = \sum_{k=1}^{3}P_kQ_k ,
$$

and it is the coefficient of the product, $\tilde P\star\tilde Q=\langle\tilde P,\tilde Q\rangle_{\natural}e_0$.

**Proposition (the form determines the product and is determined by it).** The product $\star$ and the form
$\langle\cdot,\cdot\rangle_{\natural}$ determine one another: $\tilde P\star\tilde Q=\langle\tilde P,\tilde Q\rangle_{\natural}e_0$, and
$\langle\tilde P,\tilde Q\rangle_{\natural}=\operatorname{Sc}(\tilde P\star\tilde Q)$. Consequently the structural data of the
block and of the form are the same data.

*Proof.* The two displays are the definition of the product and the reading of the scalar part of a central
value.

**Remark (the form is the scalar part of the parent product and the norm is its diagonal).** The coefficient
is the scalar part of the general quaternionic product, $\langle\tilde P,\tilde Q\rangle_{\natural}=\operatorname{Sc}(\tilde P^{\natural}\tilde Q)$,
and its diagonal is the multiplicative norm, $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\operatorname{Sc}(\tilde Q^{\natural}\tilde Q)=\tilde Q\tilde Q^{\natural}$.
The form is therefore not arbitrary on $\mathbb{B}$: it is the trace-form pairing of the quaternion factor,
and its multiplicativity property belongs to the diagonal $\langle\tilde Q\rangle_{\natural}$ and not to the bilinear form $\langle\tilde P,\tilde Q\rangle_{\natural}$. The distinction is the one the block repeats:
the diagonal $\langle\tilde Q\rangle_{\natural}$ is multiplicative and takes values whose reality depends on the elements, while the form $\langle\tilde P,\tilde Q\rangle_{\natural}$ is only bilinear.

## The Gram Matrix and the Rank

**Proposition (the Gram matrix and the rank).** In the basis $e_0,e_1,e_2,e_3$ the Gram matrix of $\langle\cdot,\cdot\rangle_{\natural}$ is the
unit matrix,

$$
G = I_4, \qquad \langle e_\mu,e_\nu\rangle_{\natural}=\delta_{\mu\nu},
$$

so $\langle\cdot,\cdot\rangle_{\natural}$ is non-degenerate of rank $4$ over $\mathbb{C}$, and its radical — the set of elements paired to zero
with the whole space — is $\{0\}$. The form is the standard symmetric form of $\mathbb{C}^4$ in the basis,
and its index over $\mathbb{R}$ is computed from the realification.

*Proof.* $\langle e_\mu,e_\nu\rangle_{\natural}=\delta_{\mu\nu}$ is the basis table of *Introduction to the Symmetric Quaternionic
Algebra of Biquaternions*, and an invertible Gram matrix is the non-degeneracy of the form. The radical is
computed in *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*.

**Remark (rank four and the centre of the algebra).** The form has rank equal to the dimension of the whole
space, and its image under the product is the central line, of complex dimension one. The rank of the form is
therefore larger than the dimension of the line on which the product takes its values, and the two numbers
must not be conflated: the form pairs all four complex directions, and the product collapses them onto one.

## The Realification and the Signature

**Proposition (the realified form).** In the real basis $e_0,e_1,e_2,e_3,ie_0,ie_1,ie_2,ie_3$ the
realification of $\langle\cdot,\cdot\rangle_{\natural}$ is the diagonal form

$$
\operatorname{diag}(I_4,-I_4),
$$

of signature $(4,4)$ and index $4$; in the interleaved basis $e_0,ie_0,e_1,ie_1,e_2,ie_2,e_3,ie_3$ it is
$\operatorname{diag}(1,-1,1,-1,1,-1,1,-1)$. The restriction to the quaternion subspace $\mathbb{H}_{\mathbb{B}}$
is positive definite of signature $(4,0)$, and the restriction to the anti-quaternion subspace
$i\mathbb{H}_{\mathbb{B}}$ is negative definite of signature $(0,4)$.

*Proof.* The form is $\mathbb{C}$-bilinear and $i$ is central, so the pairing of a real direction with its
imaginary companion is purely imaginary and drops from the realification, while $\langle ie_\mu,ie_\nu\rangle_{\natural}=-\langle e_\mu,e_\nu\rangle_{\natural}$;
the two blocks are $+I_4$ and $-I_4$ and the interleaved reading is the same matrix permuted. On
$\mathbb{H}_{\mathbb{B}}$ the form is $\sum_\mu q_\mu^2$ with $q_\mu$ real, positive definite; on
$i\mathbb{H}_{\mathbb{B}}$ it is the negative. The computation is the one of *Remarkable Subspaces under the
General Quaternionic Algebra of Biquaternions*.

**Remark (a complex form, read twice over the reals).** The signature $(4,4)$ is that of a complex bilinear
form of rank four on a complex space of dimension four, read as a real form on $\mathbb{R}^8$; the index $4$ is
half the real dimension. The two definite rows are the two halves the realification separates, and their
signatures sum to $(4,4)$. The reader is warned that the complex form is non-degenerate and has no
signature in the real sense until the realification is taken; this is the reason the complex rank and the real
signature are both recorded here.

## The Trace Form and the Absence of a Second Form

**Proposition (the trace form).** The form is the trace pairing of the parent product,

$$
\langle\tilde P,\tilde Q\rangle_{\natural} = \operatorname{Sc}\bigl(\tilde P^{\natural}\tilde Q\bigr)
= \tfrac12\operatorname{Tr}\bigl(\tilde P^{\natural}\tilde Q\bigr),
$$

and the trace of the left multiplication is the scalar part of the argument,

$$
\operatorname{Tr}\bigl(L^{\star}_{\tilde A}\bigr) = \langle\tilde A,e_0\rangle_{\natural} = A_0 .
$$

*Proof.* The first display is the remark of the first section together with the corpus identity
$\operatorname{Tr}(\tilde P\tilde Q)=2\operatorname{Sc}(\tilde P\tilde Q)$ of *Norm and Invertibility in the Symmetric Quaternionic
Algebra*. For the second, $L^{\star}_{\tilde A}e_\nu=\langle\tilde A,e_\nu\rangle_{\natural}e_0=A_\nu e_0$, so the matrix of
$L^{\star}_{\tilde A}$ in the basis has the entries $A_\nu$ at position $(0,\nu)$ and zero elsewhere; the only
nonzero diagonal entry is the one at $(0,0)$, which is $A_0$.

**Remark (there is one form and not a family).** The block carries the single form $\langle\cdot,\cdot\rangle_{\natural}$: the trace form, the
coefficient of the product, the polarisation of the norm and the Gram data $I_4$ are four readings of the same
object, and $\langle\cdot\rangle_{\natural}$ is the only form the product produces. The invariance of the next section does not select a
smaller family of forms: a symmetric $\mathbb{C}$-bilinear form $\beta$ is invariant under $\star$ exactly when
$\beta(e_0,\tilde R)=0$ for every $\tilde R$, so the invariant forms are the symmetric forms vanishing on the
central line, of complex dimension $6$, and every one of them is degenerate. There is no non-degenerate
symmetric form invariant under the product, and $\langle\cdot,\cdot\rangle_{\natural}$ itself is not invariant. The operator article *The
Multiplication Operators of the Symmetric Quaternionic Algebra* records the adjoint with respect to $\langle\cdot,\cdot\rangle_{\natural}$ and
the groups that preserve it.

## The Invariance, and Its Failure

**Definition.** The form $\langle\cdot,\cdot\rangle_{\natural}$ is **invariant under the product** when

$$
\langle\tilde P\star\tilde Q,\tilde R\rangle_{\natural} = \langle\tilde P,\tilde Q\star\tilde R\rangle_{\natural}
$$

for all $\tilde P,\tilde Q,\tilde R\in\mathbb{B}$; equivalently when
$N\bigl(\langle\tilde P,\tilde Q\rangle_{\natural}e_0,\tilde R\bigr)=N\bigl(\tilde P,\langle\tilde Q,\tilde R\rangle_{\natural}e_0\bigr)$.

**Theorem (the form is not invariant).** The form $\langle\cdot,\cdot\rangle_{\natural}$ is not invariant under $\star$. At
$\tilde P=\tilde Q=e_1$ and $\tilde R=e_0$ the two sides are $1$ and $0$:

$$
\langle\tilde P\star\tilde Q,\tilde R\rangle_{\natural}=\langle e_0,e_0\rangle_{\natural}=1, \qquad
\langle\tilde P,\tilde Q\star\tilde R\rangle_{\natural}=\langle e_1,0\rangle_{\natural}=0 .
$$

*Proof.* $e_1\star e_1=e_0$ and $e_1\star e_0=0$; the two displayed forms are then $\langle e_0,e_0\rangle_{\natural}=1$ and
$\langle e_1,0\rangle_{\natural}=0$.

**Remark (why the failure is forced).** The two sides of the invariance are
$\langle\tilde P,\tilde Q\rangle_{\natural}R_0$ and $P_0\langle\tilde Q,\tilde R\rangle_{\natural}$, and they agree for all arguments only if the
operation is associative in a way the block does not have. The failure is the same computation as the
non-vanishing associator of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*,
because $\langle\tilde P\star\tilde Q,\tilde R\rangle_{\natural}$ is the scalar part of the first bracketing of the associator. A
symmetric form that is invariant under a commutative product and has a unit is the coefficient form of a
Jordan algebra; here there is no unit and the invariance fails, which is the form-theoretic face of the
failure of the Jordan identity (*Jordan Algebras*).

## The Restriction to the Remarkable Subspaces

The restrictions of $\langle\cdot,\cdot\rangle_{\natural}$ to the remarkable subspaces are the restrictions of the quaternion form
computed in *Remarkable Subspaces under the General Quaternionic Algebra*, whose table is
quoted here; the present article adds only their reading through the product. Here $A,B\in\mathbb{C}$, $h,g$
are real quaternions, $a_0,b_0\in\mathbb{R}$ and $\vec p,\vec q\in\mathbb{R}^3$ are real vectors.

| subspace | elements | $\langle\cdot,\cdot\rangle_{\natural}$ | dimension over $\mathbb{R}$ | signature | isotropic elements |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_0$, $Be_0$ | $AB$ | $2$ | $(1,1)$ | none (complex form) |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec P$, $\vec Q$ | $(\vec P,\vec Q)$ | $6$ | $(3,3)$ | the pure zero divisors |
| $\mathbb{H}_{\mathbb{B}}$ | $h$, $g$ | $h_0g_0+\cdots+h_3g_3$ | $4$ | $(4,0)$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$, $ig$ | $-(h_0g_0+\cdots+h_3g_3)$ | $4$ | $(0,4)$ | none |
| $\mathbb{M}_+$ | $a_0e_0+i\vec p$, $b_0e_0+i\vec q$ | $a_0b_0-(\vec p,\vec q)$ | $4$ | $(1,3)$ | the elements $a_0e_0+i\vec p$ with $a_0^2=(\vec p,\vec p)$ |
| $\mathbb{M}_-$ | $ia_0e_0+\vec p$, $ib_0e_0+\vec q$ | $(\vec p,\vec q)-a_0b_0$ | $4$ | $(3,1)$ | the elements $\vec p+ia_0e_0$ with $(\vec p,\vec p)=a_0^2$ |

**Remark (the product on each restriction).** On every one of the remarkable subspaces the product of two elements is a
multiple of $e_0$ read through the displayed coefficient, and the square of an element is the value of the
restricted diagonal. The two definite rows have no isotropic element; the centre has none for the complex
form although its realification has the two real isotropic lines; the vector subspace carries the pure
zero-divisor cone; and the two Hermitian subspaces carry their real light cones. The product has no unit on
any of the remarkable subspaces, since it has none on the whole algebra.

## The Coincidence with the Hermitian Form on the Real Part

**Proposition (the coincidence on the real elements).** On two elements with real coefficients,
drawn from the quaternion subspace, the form $\langle\cdot,\cdot\rangle_{\natural}$ coincides with the Hermitian form of *The 4 Forms
over the Biquaternioid $\mathbb{C}$ Space*,

$$
\tilde P,\tilde Q\in\mathbb{H}_{\mathbb{B}} \quad\Longrightarrow\quad
\langle\tilde P,\tilde Q\rangle_{\natural} = \langle\tilde P,\tilde Q\rangle_{*}.
$$

For general complex elements the two differ: writing
$\tilde P=\tilde P'+i\tilde P''$ and $\tilde Q=\tilde Q'+i\tilde Q''$ with $\tilde P',\tilde P'',\tilde Q',\tilde Q''$ in
$\mathbb{H}_{\mathbb{B}}$, the real part of $\langle\cdot,\cdot\rangle_{\natural}$ is
$\operatorname{Re}\langle\tilde P,\tilde Q\rangle_{\natural}=\langle\tilde P',\tilde Q'\rangle_{\natural}-\langle\tilde P'',\tilde Q''\rangle_{\natural}$, which is $H$ on the real
block and $-H$ on the imaginary block, the two cross blocks being purely imaginary. Taking $\tilde P=e_0$ and
$\tilde Q=ie_0$ exhibits the difference of the two forms.

*Proof.* On real coefficients the conjugation acts trivially, $\overline{Q_0}=Q_0$ and
$\overline{\vec Q}=\vec Q$, so $\langle\tilde P,\tilde Q\rangle_{*}=P_0Q_0+(\vec P,\vec Q)=\langle\tilde P,\tilde Q\rangle_{\natural}$.
For $\tilde P=e_0$, $\tilde Q=ie_0$ one has $\langle\cdot,\cdot\rangle_{\natural}=i$ and $H=1\cdot\overline{i}= -i$, which differ.

**Remark (the collapse with the other central operation on the real part).** The coincidence is the form-level
statement that $\mathrm{SQA}=\mathrm{SPS}$ on the real part, which is one of the two collapses of the twelve
to ten recorded in *The 12 Products of the Biquaternioid Complex Space*. The symmetric part
of the plain sesquilinear product has the coefficient $\langle\tilde P,\tilde Q\rangle_{*}=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$,
which is $\langle\cdot,\cdot\rangle_{\natural}$ precisely when the coefficients are real; over $\mathbb{C}$ the two operations differ, and
$\langle\cdot,\cdot\rangle_{\natural}$ is the $\mathbb{C}$-bilinear conjugate of $\langle\cdot,\cdot\rangle_{*}$ in the second slot. The block accordingly reads the form
$\langle\cdot,\cdot\rangle_{\natural}$ as the plain form of the operation, and refers to the norm article for the Hermitian form and its
positivity.

## Summary

The form carried by the symmetric quaternionic multiplication is the quaternion form
$\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q)$, the coefficient of the product and the scalar part of the
parent product $\tilde P^{\natural}\tilde Q$. Its Gram matrix in the basis is $I_4$, so it has rank $4$ over
$\mathbb{C}$ and its radical is trivial; its realification is $\operatorname{diag}(I_4,-I_4)$ of signature
$(4,4)$ and index $4$; its restrictions to the quaternion and anti-quaternion subspaces are the two definite
rows of signatures $(4,0)$ and $(0,4)$; its restrictions to the other four subspaces have signatures
$(1,1)$, $(3,3)$, $(1,3)$ and $(3,1)$ and carry the isotropic elements recorded in the table. The form is the
trace form, $\langle\cdot,\cdot\rangle_{\natural}=\operatorname{Sc}(\tilde P^{\natural}\tilde Q)=\tfrac12\operatorname{Tr}(\tilde P^{\natural}\tilde Q)$,
and the trace of a left multiplication is the scalar part, $\operatorname{Tr}(L^{\star}_{\tilde A})=A_0$. The
form is **not** invariant under the product, the two sides of $\langle\tilde P\star\tilde Q,\tilde R\rangle_{\natural}=\langle\tilde P,\tilde Q\star\tilde R\rangle_{\natural}$
being $1$ and $0$ at $e_1,e_1,e_0$, which is the form-theoretic face of the failure of the Jordan identity.
On the real elements the form coincides with the Hermitian form $\langle\cdot,\cdot\rangle_{*}$, which is the form-level statement of the
collapse $\mathrm{SQA}=\mathrm{SPS}$ on the real part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde P,\tilde Q\rangle_{\natural}=P_0Q_0+(\vec P,\vec Q)$ | the quaternion form of the block, the coefficient of the product |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the norm form, the diagonal of $\langle\cdot,\cdot\rangle_{\natural}$ |
| $\langle\tilde P,\tilde Q\rangle_{*}=P_0\overline{Q_0}+(\vec P,\overline{\vec Q})$ | the Hermitian form of $\mathbb{B}$ |
| $G=I_4$ | the Gram matrix of $\langle\cdot,\cdot\rangle_{\natural}$ in the basis $e_0,e_1,e_2,e_3$ |
| $\operatorname{diag}(I_4,-I_4)$, signature $(4,4)$ | the realification of $\langle\cdot,\cdot\rangle_{\natural}$ |
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the signatures of the restrictions to the remarkable subspaces |
| $L^{\star}_{\tilde A}$, $\operatorname{Tr}(L^{\star}_{\tilde A})=A_0$ | the left multiplication and its trace |
| $\langle\tilde P\star\tilde Q,\tilde R\rangle_{\natural}=\langle\tilde P,\tilde Q\star\tilde R\rangle_{\natural}$ | the invariance that fails |

## Further Reading

- *The 4 Forms over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternioid-c-space.md`), for the quaternion form among the four pairings
- *Comparison Between the Four General Products* (`articles_maths/comparison-between-the-four-general-products.md`), for the quaternion form beside the other three coefficients
- *Norm and Invertibility in the General Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-general-quaternionic-algebra.md`), for the norm, the polarisation and the Hermitian form
- *Remarkable Subspaces under the General Quaternionic Algebra* (`articles_maths/remarkable-subspaces-under-the-general-quaternionic-algebra.md`), for the restriction Gram matrices and the signatures
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the radical and the isotropic elements
- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), for the adjoint with respect to $\langle\cdot,\cdot\rangle_{\natural}$ and the groups preserving it
