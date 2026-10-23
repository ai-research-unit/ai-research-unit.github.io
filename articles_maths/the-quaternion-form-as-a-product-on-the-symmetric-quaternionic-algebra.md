# __The Quaternion Form as a Product on the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic multiplication is a form placed on the central line: the value of
$\tilde Q_1\star\tilde Q_2$ is the central element $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, and the whole content of the
operation is the coefficient $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$
(*Introduction to the Symmetric Quaternionic Algebra*). This article reads the coefficient
as the **form that the block carries**: it identifies it, computes its Gram matrix and its rank, its
realification and its signature, its invariance under the product and the failure of that invariance, its
restriction to the remarkable subspaces, and its relation to the Hermitian form $\langle\cdot,\cdot\rangle_{*}$ of the algebra.

The form $\langle\cdot,\cdot\rangle_{\natural}$ is the quaternion form named in the catalogue *The 12 Products of the Biquaternion Complex Space*, and it is the general quaternionic bilinear one of the four pairings of *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; its diagonal is the norm of *Norm and Invertibility in the General Quaternionic Algebra*, and on the remarkable subspaces its restrictions and their signatures are
*Remarkable Subspaces under the General Quaternionic Algebra*, whose table is quoted here and
not recomputed. The article therefore owns the reading of the form **as the form of the product** — the Gram
data, the invariance question and the coincidence with $\langle\cdot,\cdot\rangle_{*}$ — and cites the norm article and the remarkable-subspace
article for the form itself. The Hermitian form $\langle\cdot,\cdot\rangle_{*}$ is *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; the invariance
question for a symmetric product is *Jordan Algebras*; the matrix reading of the same form is
*Introduction to the Symmetric Quaternionic Algebra*.

## The Form Read as a Product

**Definition.** The **quaternion form** of the block is the symmetric $\mathbb{C}$-bilinear form

$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = Q_{1t}Q_{2t} + (\vec Q_1,\vec Q_2), \qquad
(\vec Q_1,\vec Q_2) = \sum_{k\in\{x,y,z\}}Q_{1,k}Q_{2,k} ,
$$

and it is the coefficient of the product, $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$.

**Proposition (the form determines the product and is determined by it).** The product $\star$ and the form
$\langle\cdot,\cdot\rangle_{\natural}$ determine one another: $\tilde Q_1\star\tilde Q_2=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t$, and
$\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\operatorname{Sc}(\tilde Q_1\star\tilde Q_2)$. Consequently the structural data of the
block and of the form are the same data.

*Proof.* The two displays are the definition of the product and the reading of the scalar part of a central
value.

**Remark (the form is the scalar part of the parent product and the norm is its diagonal).** The coefficient
is the scalar part of the general quaternionic product, $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\operatorname{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$,
and its diagonal is the multiplicative norm, $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\operatorname{Sc}(\tilde Q^{\natural}\tilde Q)=\tilde Q\tilde Q^{\natural}$.
The form is therefore not arbitrary on $\mathbb{B}$: it is the trace-form pairing of the quaternion factor,
and its multiplicativity property belongs to the diagonal $\langle\tilde Q\rangle_{\natural}$ and not to the bilinear form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$. The distinction is the one the block repeats:
the diagonal $\langle\tilde Q\rangle_{\natural}$ is multiplicative and takes values whose reality depends on the elements, while the form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$ is only bilinear.

## The Gram Matrix and the Rank

**Proposition (the Gram matrix and the rank).** In the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ the Gram matrix of $\langle\cdot,\cdot\rangle_{\natural}$ is the
unit matrix,

$$ \boxed{\; G = I_4, \qquad \langle e_\mu,e_\nu\rangle_{\natural}=\delta_{\mu\nu} \;}, $$

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

**Proposition (the realified form).** In the real basis $e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z$ the
realification of $\langle\cdot,\cdot\rangle_{\natural}$ is the diagonal form

$$
\operatorname{diag}(I_4,-I_4),
$$

of signature $(4,4)$ and index $4$; in the interleaved basis $e_t,ie_t,\vec e_x,i\vec e_x,\vec e_y,i\vec e_y,\vec e_z,i\vec e_z$ it is
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
\boxed{\;
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \operatorname{Sc}\bigl(\tilde Q_1^{\natural}\tilde Q_2\bigr)
= \tfrac12\operatorname{Tr}\bigl(\tilde Q_1^{\natural}\tilde Q_2\bigr)
\;},
$$

and the trace of the left multiplication is the scalar part of the argument,

$$
\operatorname{Tr}\bigl(L^{\star}_{\tilde Q_4}\bigr) = \langle\tilde Q_4,e_t\rangle_{\natural} = Q_{4t} .
$$

*Proof.* The first display is the remark of the first section together with the corpus identity
$\operatorname{Tr}(\tilde Q_1\tilde Q_2)=2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ of *Norm and Invertibility in the Symmetric Quaternionic
Algebra*. For the second, $L^{\star}_{\tilde Q_4}e_\nu=\langle\tilde Q_4,e_\nu\rangle_{\natural}e_t=Q_{4\nu} e_t$, so the matrix of
$L^{\star}_{\tilde Q_4}$ in the basis has the entries $Q_{4\nu}$ at position $(t,\nu)$ and zero elsewhere; the only
nonzero diagonal entry is the one at $(t,t)$, which is $Q_{4t}$.

**Remark (there is one form and not a family).** The block carries the single form $\langle\cdot,\cdot\rangle_{\natural}$: the trace form, the
coefficient of the product, the polarisation of the norm and the Gram data $I_4$ are four readings of the same
object, and $\langle\cdot\rangle_{\natural}$ is the only form the product produces. The invariance of the next section does not select a
smaller family of forms: a symmetric $\mathbb{C}$-bilinear form $\beta$ is invariant under $\star$ exactly when
$\beta(e_t,\tilde Q_3)=0$ for every $\tilde Q_3$, so the invariant forms are the symmetric forms vanishing on the
central line, of complex dimension $6$, and every one of them is degenerate. There is no non-degenerate
symmetric form invariant under the product, and $\langle\cdot,\cdot\rangle_{\natural}$ itself is not invariant. The operator article *The
Multiplication Operators of the Symmetric Quaternionic Algebra* records the adjoint with respect to $\langle\cdot,\cdot\rangle_{\natural}$ and
the groups that preserve it.

## The Invariance, and Its Failure

**Definition.** The form $\langle\cdot,\cdot\rangle_{\natural}$ is **invariant under the product** when

$$
\langle\tilde Q_1\star\tilde Q_2,\tilde Q_3\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_2\star\tilde Q_3\rangle_{\natural}
$$

for all $\tilde Q_1,\tilde Q_2,\tilde Q_3\in\mathbb{B}$; equivalently when
$N\bigl(\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}e_t,\tilde Q_3\bigr)=N\bigl(\tilde Q_1,\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}e_t\bigr)$.

**Theorem (the form is not invariant).** The form $\langle\cdot,\cdot\rangle_{\natural}$ is not invariant under $\star$. At
$\tilde Q_1=\tilde Q_2=\vec e_x$ and $\tilde Q_3=e_t$ the two sides are $1$ and $0$:

$$
\langle\tilde Q_1\star\tilde Q_2,\tilde Q_3\rangle_{\natural}=\langle e_t,e_t\rangle_{\natural}=1, \qquad
\langle\tilde Q_1,\tilde Q_2\star\tilde Q_3\rangle_{\natural}=\langle \vec e_x,0\rangle_{\natural}=0 .
$$

*Proof.* $\vec e_x\star \vec e_x=e_t$ and $\vec e_x\star e_t=0$; the two displayed forms are then $\langle e_t,e_t\rangle_{\natural}=1$ and
$\langle \vec e_x,0\rangle_{\natural}=0$.

**Remark (why the failure is forced).** The two sides of the invariance are
$\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}Q_{3t}$ and $Q_{1t}\langle\tilde Q_2,\tilde Q_3\rangle_{\natural}$, and they agree for all arguments only if the
operation is associative in a way the block does not have. The failure is the same computation as the
non-vanishing associator of *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*,
because $\langle\tilde Q_1\star\tilde Q_2,\tilde Q_3\rangle_{\natural}$ is the scalar part of the first bracketing of the associator. A
symmetric form that is invariant under a commutative product and has a unit is the coefficient form of a
Jordan algebra; here there is no unit and the invariance fails, which is the form-theoretic face of the
failure of the Jordan identity (*Jordan Algebras*).

## The Restriction to the Remarkable Subspaces

The restrictions of $\langle\cdot,\cdot\rangle_{\natural}$ to the remarkable subspaces are the restrictions of the quaternion form
computed in *Remarkable Subspaces under the General Quaternionic Algebra*, whose table is
quoted here; the present article adds only their reading through the product. Here $A,B\in\mathbb{C}$, $h,g$
are real quaternions, $a_t,b_t\in\mathbb{R}$ and $\vec p,\vec q\in\mathbb{R}^3$ are real vectors.

| subspace | elements | $\langle\cdot,\cdot\rangle_{\natural}$ | dimension over $\mathbb{R}$ | signature | isotropic elements |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_t$, $Be_t$ | $AB$ | $2$ | $(1,1)$ | none (complex form) |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec Q_1$, $\vec Q_2$ | $(\vec Q_1,\vec Q_2)$ | $6$ | $(3,3)$ | the pure zero divisors |
| $\mathbb{H}_{\mathbb{B}}$ | $h$, $g$ | $h_tg_t+h_xg_x+h_yg_y+h_zg_z$ | $4$ | $(4,0)$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$, $ig$ | $-(h_tg_t+h_xg_x+h_yg_y+h_zg_z)$ | $4$ | $(0,4)$ | none |
| $\mathbb{M}_+$ | $a_te_t+i\vec p$, $b_te_t+i\vec q$ | $a_tb_t-(\vec p,\vec q)$ | $4$ | $(1,3)$ | the elements $a_te_t+i\vec p$ with $a_t^2=(\vec p,\vec p)$ |
| $\mathbb{M}_-$ | $ia_te_t+\vec p$, $ib_te_t+\vec q$ | $(\vec p,\vec q)-a_tb_t$ | $4$ | $(3,1)$ | the elements $\vec p+ia_te_t$ with $(\vec p,\vec p)=a_t^2$ |

**Remark (the product on each restriction).** On every one of the remarkable subspaces the product of two elements is a
multiple of $e_t$ read through the displayed coefficient, and the square of an element is the value of the
restricted diagonal. The two definite rows have no isotropic element; the centre has none for the complex
form although its realification has the two real isotropic lines; the vector subspace carries the pure
zero-divisor cone; and the two Hermitian subspaces carry their real null cones. The product has no unit on
any of the remarkable subspaces, since it has none on the whole algebra.

## The Coincidence with the Hermitian Form on the Real Part

**Proposition (the coincidence on the real elements).** On two elements with real coefficients,
drawn from the quaternion subspace, the form $\langle\cdot,\cdot\rangle_{\natural}$ coincides with the Hermitian form of *The 4 Forms
over the Biquaternion $\mathbb{C}$ Space*,

$$
\boxed{\;
\tilde Q_1,\tilde Q_2\in\mathbb{H}_{\mathbb{B}} \quad\Longrightarrow\quad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \langle\tilde Q_1,\tilde Q_2\rangle_{*}
\;}.
$$

For general complex elements the two differ: writing
$\tilde Q_1=\tilde Q_{1,\mathrm{Re}}+i\tilde Q_{1,\mathrm{Im}}$ and $\tilde Q_2=\tilde Q_{\mathrm{Re}}+i\tilde Q_{\mathrm{Im}}$ with $\tilde Q_{1,\mathrm{Re}},\tilde Q_{1,\mathrm{Im}},\tilde Q_{\mathrm{Re}},\tilde Q_{\mathrm{Im}}$ in
$\mathbb{H}_{\mathbb{B}}$, the real part of $\langle\cdot,\cdot\rangle_{\natural}$ is
$\operatorname{Re}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_{1,\mathrm{Re}},\tilde Q_{\mathrm{Re}}\rangle_{\natural}-\langle\tilde Q_{1,\mathrm{Im}},\tilde Q_{\mathrm{Im}}\rangle_{\natural}$, which is $H$ on the real
block and $-H$ on the imaginary block, the two cross blocks being purely imaginary. Taking $\tilde Q_1=e_t$ and
$\tilde Q=ie_t$ exhibits the difference of the two forms.

*Proof.* On real coefficients the conjugation acts trivially, $\overline{Q_t}=Q_t$ and
$\overline{\vec Q_2}=\vec Q_2$, so $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$.
For $\tilde Q_1=e_t$, $\tilde Q_2=ie_t$ one has $\langle\cdot,\cdot\rangle_{\natural}=i$ and $H=1\cdot\overline{i}= -i$, which differ.

**Remark (the collapse with the other central operation on the real part).** The coincidence is the form-level
statement that $\mathrm{SQA}=\mathrm{SPS}$ on the real part, which is one of the two collapses of the twelve
to ten recorded in *The 12 Products of the Biquaternion Complex Space*. The symmetric part
of the plain sesquilinear product has the coefficient $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$,
which is $\langle\cdot,\cdot\rangle_{\natural}$ precisely when the coefficients are real; over $\mathbb{C}$ the two operations differ, and
$\langle\cdot,\cdot\rangle_{\natural}$ is the $\mathbb{C}$-bilinear conjugate of $\langle\cdot,\cdot\rangle_{*}$ in the second slot. The block accordingly reads the form
$\langle\cdot,\cdot\rangle_{\natural}$ as the plain form of the operation, and refers to the norm article for the Hermitian form and its
positivity.

## Summary

The form carried by the symmetric quaternionic multiplication is the quaternion form
$\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$, the coefficient of the product and the scalar part of the
parent product $\tilde Q_1^{\natural}\tilde Q_2$. Its Gram matrix in the basis is $I_4$, so it has rank $4$ over
$\mathbb{C}$ and its radical is trivial; its realification is $\operatorname{diag}(I_4,-I_4)$ of signature
$(4,4)$ and index $4$; its restrictions to the quaternion and anti-quaternion subspaces are the two definite
rows of signatures $(4,0)$ and $(0,4)$; its restrictions to the other four subspaces have signatures
$(1,1)$, $(3,3)$, $(1,3)$ and $(3,1)$ and carry the isotropic elements recorded in the table. The form is the
trace form, $\langle\cdot,\cdot\rangle_{\natural}=\operatorname{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\tfrac12\operatorname{Tr}(\tilde Q_1^{\natural}\tilde Q_2)$,
and the trace of a left multiplication is the scalar part, $\operatorname{Tr}(L^{\star}_{\tilde Q_4})=Q_{4t}$. The
form is **not** invariant under the product, the two sides of $\langle\tilde Q_1\star\tilde Q_2,\tilde Q_3\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\star\tilde Q_3\rangle_{\natural}$
being $1$ and $0$ at $\vec e_x,\vec e_x,e_t$, which is the form-theoretic face of the failure of the Jordan identity.
On the real elements the form coincides with the Hermitian form $\langle\cdot,\cdot\rangle_{*}$, which is the form-level statement of the
collapse $\mathrm{SQA}=\mathrm{SPS}$ on the real part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=Q_{1t}Q_{2t}+(\vec Q_1,\vec Q_2)$ | the quaternion form of the block, the coefficient of the product |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^2$ | the norm form, the diagonal of $\langle\cdot,\cdot\rangle_{\natural}$ |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=Q_{1t}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | the Hermitian form of $\mathbb{B}$ |
| $G=I_4$ | the Gram matrix of $\langle\cdot,\cdot\rangle_{\natural}$ in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $\operatorname{diag}(I_4,-I_4)$, signature $(4,4)$ | the realification of $\langle\cdot,\cdot\rangle_{\natural}$ |
| $(1,1),(3,3),(4,0),(0,4),(1,3),(3,1)$ | the signatures of the restrictions to the remarkable subspaces |
| $L^{\star}_{\tilde Q_4}$, $\operatorname{Tr}(L^{\star}_{\tilde Q_4})=Q_{4t}$ | the left multiplication and its trace |
| $\langle\tilde Q_1\star\tilde Q_2,\tilde Q_3\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\star\tilde Q_3\rangle_{\natural}$ | the invariance that fails |

## Further Reading

- [The 4 Forms over the Biquaternion $\mathbb{C}$ Space](the-4-forms-over-the-biquaternion-c-space.html), for the quaternion form among the four pairings
- [Comparison Between the Four General Products](comparison-between-the-four-general-products.html), for the quaternion form beside the other three coefficients
- [Norm and Invertibility in the General Quaternionic Algebra](norm-and-invertibility-in-the-general-quaternionic-algebra.html), for the norm, the polarisation and the Hermitian form
- [Remarkable Subspaces under the General Quaternionic Algebra](remarkable-subspaces-under-the-general-quaternionic-algebra.html), for the restriction Gram matrices and the signatures
- [The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra](the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.html), for the radical and the isotropic elements
- [The Multiplication Operators of the Symmetric Quaternionic Algebra](the-multiplication-operators-of-the-symmetric-quaternionic-algebra.html), for the adjoint with respect to $\langle\cdot,\cdot\rangle_{\natural}$ and the groups preserving it
