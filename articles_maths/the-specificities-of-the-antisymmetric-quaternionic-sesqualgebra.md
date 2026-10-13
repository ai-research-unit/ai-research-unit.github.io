# __The Specificities of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

Of the twelve operations of the corpus the block is the one whose value is the conjugate cross product alone, with neither a scalar part nor a mixed term, and the question of this article is the discriminating one: **what does the block have that the other eleven do not?** The answer is a law against the form of the row, and it is the classical property of the cross product read in the sesquilinear setting:

**the value of the block is orthogonal to its own second argument in the Krein form,**

$$
K(\tilde X\diamond\tilde Y,\tilde Y)=0 \qquad\text{for all }\tilde X,\tilde Y ,
$$

with $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ the Krein form of the row. The law holds for the block and for no other of the twelve; it is equivalent to the statement that the form induced by the left multiplication, $\beta_{\tilde X}(\tilde Y,\tilde Z)=K(\tilde X\diamond\tilde Y,\tilde Z)$, is alternating, and to the statement that the conjugate-linear left multiplication is skew-adjoint for $K$; and it is the source of the element theory of the block, since the absence of the unit, the emptiness of the roots of the central values, the absence of the nontrivial idempotents and the index of the nilpotents are all derived from it in one line each.

The criterion is different in kind from the one of the model block. For the plain algebra the discriminating law is the left alternativity of the product, a law of the multiplication alone; for the block the discriminating law is a law of the multiplication against the form, and no law of the multiplication alone separates it from the symmetric half of its own row, as the isolation below shows. The block is therefore the member of the twelve whose specificity is form-theoretic, and this is the reason the article is the last of the block: it collects the law, isolates the block among the twelve, and points to the element theory the law governs.

The form and its pairing with the block are *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*; the operator form of the law is *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*; the element theory it delivers is *Norm and Invertibility*, *Zero Divisors in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Square Roots of Minus One, Zero and Plus One in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Square Roots of a General Element in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, *Idempotents in the 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*; the twelve products are *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *The 12 Products of the Biquaternion Complex Space*; and the model article of the same construction is *The Specificities of the General Plain Algebra*.

**Conventions.** As in the block: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$ and $e_k^2=-e_0$, a generic element $\tilde Q=Q_0e_0+\mathbf{Q}$, and the product $\diamond$ for the block, $\tilde P\diamond\tilde Q=\mathbf{P}\times\overline{\mathbf{Q}}$. The Krein form is $K(\tilde P,\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ with $\varepsilon_0=1$ and $\varepsilon_k=-1$, linear in the first argument and conjugate-linear in the second, and the complex bilinear dot product of two vector parts is $(\mathbf{A},\mathbf{B})=\sum_kA_kB_k$. The other products are named by their three-letter codes when they are named at all, and the vector subspace $\mathrm{Vect}(\mathbb{B})$ is the complex span of $e_1,e_2,e_3$.

## The Definition, Relative to a Form

**Definition (the law of a product against a form).** Let $\star$ be a product on $\mathbb{B}$ and let $\beta$ be a form on $\mathbb{B}$. The product $\star$ is **$\beta$-orthogonal to its second argument** when

$$
\beta(x\star y,y)=0 \qquad\text{for all }x,y\in\mathbb{B}.
$$

The **induced form** of $\star$ by $\beta$ at an element $x$ is the form $\beta_x(y,z)=\beta(x\star y,z)$ in the two remaining arguments.

**Definition (alternating form).** A form $\gamma$ in two arguments is **alternating** when $\gamma(y,y)=0$ for every $y$; when $\gamma$ is conjugate-linear in both arguments this is equivalent to the antisymmetry $\gamma(y,z)+\gamma(z,y)=0$.

The law is read for the block with the Krein form $K$ and with the induced forms $K_{\tilde X}(\tilde Y,\tilde Z)=K(\tilde X\diamond\tilde Y,\tilde Z)$. The form $K$ is conjugate-linear in its second argument and the block is conjugate-linear in its second slot, so the induced form is conjugate-linear in each of its two arguments, and the alternating condition for it is the antisymmetry with no conjugation, as in the second definition.

## The Law of the Block

**Theorem (the block is $K$-orthogonal to its second argument).** For all biquaternions,

$$
K(\tilde X\diamond\tilde Y,\tilde Y)=0 .
$$

*Proof.* By the rule of the block, $\tilde X\diamond\tilde Y=\mathbf{X}\times\overline{\mathbf{Y}}$ is a pure vector, so its scalar coordinate is zero and the pairing reads $K(\tilde X\diamond\tilde Y,\tilde Y)=-(\mathbf{X}\times\overline{\mathbf{Y}},\overline{\mathbf{Y}})$, the complex bilinear dot product of the value with the conjugate of the vector part of the second argument. The cross product is orthogonal to its second entry in the bilinear dot, $(\mathbf{a}\times\mathbf{b},\mathbf{b})=0$ for all $\mathbf{a},\mathbf{b}$, and the identity with $\mathbf{a}=\mathbf{X}$ and $\mathbf{b}=\overline{\mathbf{Y}}$ gives the vanishing.

**Corollary (the induced form is alternating).** For all biquaternions,

$$
K(\tilde X\diamond\tilde Y,\tilde Z)+K(\tilde X\diamond\tilde Z,\tilde Y)=0 ,
$$

that is, the form induced by the block at each element is alternating; equivalently,

$$
K(\tilde X\diamond\tilde Y,\tilde Z)=-K(\tilde X\diamond\tilde Z,\tilde Y).
$$

*Proof.* The identity follows from the law by the expansion of the diagonal of the induced form: the form $K_{\tilde X}$ is conjugate-linear in each argument, so $K_{\tilde X}(\tilde Y+\tilde Z,\tilde Y+\tilde Z)$ expands into the four terms and the two diagonal terms vanish by the law, leaving $K_{\tilde X}(\tilde Y,\tilde Z)+K_{\tilde X}(\tilde Z,\tilde Y)=0$.

**Corollary (the left multiplication is skew-adjoint).** For every $\tilde X$ the conjugate-linear left multiplication $L_{\tilde X}$ of the block satisfies

$$
L_{\tilde X}^{\dagger}=-L_{\tilde X}
$$

for the adjoint with respect to the Krein form: the left multiplication is the negative of its own adjoint.

*Proof.* The adjoint of a conjugate-linear map $T$ with respect to $K$ is defined by the identity $K(T\tilde Y,\tilde Z)=\overline{K(\tilde Y,T^{\dagger}\tilde Z)}$ in the conjugate-linear class, as *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra* records. With $T=L_{\tilde X}$ and $T^{\dagger}=-L_{\tilde X}$ the identity reads $K(\tilde X\diamond\tilde Y,\tilde Z)=-\overline{K(\tilde Y,\tilde X\diamond\tilde Z)}$, and the pairing is conjugate-symmetric, $K(\tilde Y,\tilde W)=\overline{K(\tilde W,\tilde Y)}$, so the right-hand side is $-K(\tilde X\diamond\tilde Z,\tilde Y)$, which is the alternating identity of the corollary above. The reading of the adjoints and the class of the definition are *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, where the adjoint of the left multiplication is computed and is the negative of the operator.

**Remark (the law is the perpendicularity of the cross product).** The law is not an accident of the choice of the form: it is the classical statement that the cross product of two vectors is perpendicular to each of them, read through the form of the row. In the bilinear reading the cross product is orthogonal to both entries of the bilinear dot, and the second of the two orthogonality statements is the one that the pairing of the block carries, the conjugation of the second slot of the block and the conjugation of the second slot of the form matching so that the scalar coordinate of the value drops out. The block is thus the member of the twelve in which the geometric content of the cross product survives the transfer to the sesquilinear class, and the law is the whole of that survival.

## The Isolation among the Twelve

**Theorem (no other product of the twelve satisfies the law).** For each of the eleven products $\star\neq\diamond$ there are biquaternions $\tilde X,\tilde Y$ with

$$
K(\tilde X\star\tilde Y,\tilde Y)\neq0 .
$$

*Proof.* The witnesses are in the table, one entry per family; each is verified by the computation of the product and of the pairing, and the failure is genuine, that is the pairing is not zero and not merely undefined.

| family | $K(\tilde X\star\tilde Y,\tilde Y)$ | the witness |
|---|---|---|
| GPA | $2i$ | $\tilde X=e_1$, $\tilde Y=e_2+ie_3$ |
| GQA | $2i$ | $\tilde X=e_2$, $\tilde Y=e_1+ie_3$ |
| APA | $-2i$ | $\tilde X=e_2$, $\tilde Y=e_1+ie_3$ |
| AQA | $2i$ | $\tilde X=e_2$, $\tilde Y=e_1+ie_3$ |
| SPA | $-2$ | $\tilde X=e_1$, $\tilde Y=e_0+e_1$ |
| SQA, SPS | $1$ | $\tilde X=e_1$, $\tilde Y=e_0+e_1$ |
| APS | $-1$ | $\tilde X=e_1$, $\tilde Y=e_0+e_1$ |
| GPS, GQS, SQS | $1$ | $\tilde X=e_0$, $\tilde Y=e_1$ |
| **AQS** | $0$ at every pair | the law holds |

The eleven failures separate by where the failure enters. Four fail already on the vector subspace: the two products of the bilinear rows, $\mathrm{GPA}$ and $\mathrm{GQA}$, whose second slot is not conjugated, together with their antisymmetric parts $\mathrm{APA}$ and $\mathrm{AQA}$. For these four the value on two pure vectors carries the cross product $\mathbf{P}\times\mathbf{Q}$ **without** the conjugation of the second argument, while the pairing is read against the conjugate of that argument, so the orthogonality of the cross product is not the orthogonality the form asks for. The other seven fail only off the vector subspace, at pairs in which at least one argument has a nonzero scalar coordinate: the four symmetric halves, whose value on two pure vectors is central, and the antisymmetric plain sesqualgebra $\mathrm{APS}$ with the two general sesquilinear products $\mathrm{GPS}$ and $\mathrm{GQS}$, whose value on two pure vectors is carried by the conjugate cross product. The block is the one product whose value is the cross product with the conjugate of the second argument, and the conjugation of the second slot of the block and the conjugation of the second slot of the form act in the same direction on the same entry.

**Remark (the criterion is the law on the whole space).** Restricted to the pairs of pure vectors the law holds for $\mathrm{SPA}$, $\mathrm{SQA}$, $\mathrm{SPS}$, $\mathrm{SQS}$, $\mathrm{GPS}$, $\mathrm{APS}$, $\mathrm{GQS}$ and the block, and fails for $\mathrm{GPA}$, $\mathrm{GQA}$, $\mathrm{APA}$ and $\mathrm{AQA}$. It holds for the four symmetric halves because on pure arguments their values are central, and a central value is orthogonal to every pure vector in a form that reads the scalar coordinate with the sign $+1$; it holds for $\mathrm{GPS}$, $\mathrm{APS}$, $\mathrm{GQS}$ and the block because the values on pure arguments are carried by the conjugate cross product, whose second entry is exactly the argument the form reads. The block is therefore not distinguished by the restriction, and the criterion is the law on the whole space, where it is alone.

## What the Law Delivers

The law is the source of the element theory of the block, and the four deliveries below are one line each; each is computed in its own article.

**No unit.** Suppose the block had a left unit $e$, so that $e\diamond\tilde X=\tilde X$ for every $\tilde X$. The law reads $K(e\diamond\tilde X,\tilde X)=K(\tilde X,\tilde X)=0$ for every $\tilde X$, so every element would be isotropic for $K$; but $K(e_0,e_0)=1$, the unit of the parent algebra lying on the positive definite row of the form. The block has no left unit, and by the mirror reading no right unit. The element theory is *Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra*.

**No root of a nonzero central value.** Suppose $\tilde X\diamond\tilde X=\lambda e_0$ with $\lambda\neq0$. The law with the pair $(\tilde X,\tilde X)$ reads $K(\lambda e_0,\tilde X)=\lambda\overline{X_0}=0$, so $X_0=0$; the square of an element with vanishing scalar coordinate is a pure vector, and it cannot be the nonzero central element $\lambda e_0$. The roots of $+1$, of $-1$ and of every nonzero central value are empty, and the roots of $0$ are the cone of the diagonal. The three equations are *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Sesqualgebra*.

**No nontrivial idempotent.** Suppose $\tilde X\diamond\tilde X=\tilde X$ with $\tilde X\neq0$. The law with the pair $(\tilde X,\tilde X)$ reads $K(\tilde X,\tilde X)=0$, so $\tilde X$ is isotropic for $K$; and $\tilde X$ is a value of the block, so $X_0=0$, and the isotropy of a pure vector reads $-(\mathbf{X},\overline{\mathbf{X}})=0$, that is the vanishing of the non-negative real sum $\sum_k\lvert X_k\rvert^{2}$, which gives $\mathbf{X}=0$. The only idempotent of the block is the origin. The idempotent set and the absent projector calculus are *Idempotents of the Antisymmetric Quaternionic Sesqualgebra*.

**The index of the nilpotents is two or four.** The law written on the vector subspace is the orthogonality $(\mathbf{X}\times\overline{\mathbf{Y}},\overline{\mathbf{Y}})=0$ of the value to the conjugate of the second argument, and it is the identity that closes the recurrence of the left-nested powers of the block, $\mathbf{u}_{k+2}=-\overline{c}\,\mathbf{u}_k$ from the second power on, out of which the index two and the index four follow. The two classes and the recurrence are *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*.

**Remark (the law and the zero divisors).** One delivery of the element theory is not a consequence of the law: the fact that every nonzero element of the block is a two-sided zero divisor, with the annihilation pair $(\tilde A,\overline{\tilde A})$, is the reading of the rule and not of the law against the form. The law delivers the information on the diagonal of the multiplication, and the zero divisors are read on the off-diagonal pair of the element with its conjugate; the two are compared in *Zero Divisors of the Antisymmetric Quaternionic Sesqualgebra*, and the comparison is the reason the article is not a corollary of this one.

## The Placement of the Criterion

**The criterion is form-theoretic and the block is the form-theoretic member of the twelve.** The specificities of the other blocks are laws of the multiplication alone: the plain algebra is the one that is left-alternative, the antisymmetric plain algebra is the one whose bracket is a Lie bracket, and so on. The block is separated from the eleven by a law in which the multiplication and the form of the row appear together, and no law of the multiplication alone separates it: the block and the symmetric half of its row differ in the symmetry alone, and the two agree on the vector subspace, where the restricted law holds for both, so that the reading of the difference needs the form. This is the sense in which the article is the last of the block: the criterion is stated on the object that the block shares with the row, the form, and the element theory of the block is the list of its consequences.

**The structural reading.** The law says that the block never produces a value in the direction of its own second argument, in the form of the row: the value is orthogonal to the argument it is paired with. The block is therefore the member of the twelve that is *purely transverse*, and the whole of its element theory is the reading of that transversality: the diagonal is the value orthogonal to its own argument, hence isotropic and hence never central; the off-diagonal pairs are orthogonal to their second arguments, hence never invertible; and the powers are orthogonal at every step, hence terminate at two or at four. The antisymmetrisation of the quaternionic sesquilinear product is the operation that installs the transversality, and the block is the image of the row under it.

**The isolation is form-theoretic.** The law is the only criterion of the block that is not a law of the multiplication alone, and it is the one that separates the block from the symmetric half of its own row: the two agree on the vector subspace, and the reading of the difference needs the form. The collection of the twelve is *The 12 Products of the Biquaternion Complex Space*, read through the criteria of *The Specificities of the General Plain Algebra*, *The Specificities of the General Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic Algebra*.

## Summary

The block is the product of the twelve that is $K$-orthogonal to its own second argument: $K(\tilde X\diamond\tilde Y,\tilde Y)=0$ for all biquaternions, with $K$ the Krein form of the row. The law is equivalent to the alternating character of the induced form $K_{\tilde X}(\tilde Y,\tilde Z)=K(\tilde X\diamond\tilde Y,\tilde Z)$ and to the skew-adjointness of the conjugate-linear left multiplication, $L_{\tilde X}^{\dagger}=-L_{\tilde X}$; it is the classical perpendicularity of the cross product transferred to the sesquilinear class; and it is satisfied by no other of the twelve, each of the other eleven failing on a witness. The law restricted to the pairs of pure vectors holds for eight of the twelve, so the criterion is the law on the whole space. The law delivers the element theory of the block: no unit, since a unit would make every element isotropic for a form that is positive at $e_0$; no root of a nonzero central value; no nontrivial idempotent, the isotropy together with the purity forcing the origin; and the index of the nilpotents at two and at four, through the recurrence of the left-nested powers. The zero-divisor set of the block is read from the rule and not from the law, and the criterion is form-theoretic, which is what separates the block from the symmetric half of its own row and makes the article the last of the block.

## Summary of Notation

| symbol | meaning |
|---|---|
| $K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, linear in the first argument |
| $K(\tilde X\diamond\tilde Y,\tilde Y)=0$ | the law of the block |
| $K_{\tilde X}(\tilde Y,\tilde Z)=K(\tilde X\diamond\tilde Y,\tilde Z)$ | the induced form at an element |
| $K(\tilde X\diamond\tilde Y,\tilde Z)=-K(\tilde X\diamond\tilde Z,\tilde Y)$ | the alternating character of the induced form |
| $L_{\tilde X}^{\dagger}=-L_{\tilde X}$ | the skew-adjointness of the left multiplication |
| $(\mathbf{A},\mathbf{B})=\sum_kA_kB_k$ | the complex bilinear dot product |
| $\tilde X=e_1$, $\tilde Y=e_2+ie_3$ | the witness for GPA |
| $\tilde X=e_2$, $\tilde Y=e_1+ie_3$ | the witness for GQA, APA and AQA |
| $\tilde X=e_1$, $\tilde Y=e_0+e_1$ | the witness for SPA, SQA, SPS and APS |
| $\tilde X=e_0$, $\tilde Y=e_1$ | the witness for GPS, GQS and SQS |

## Further Reading

- *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*, for the Krein form, the pairing of a value with a third element and the invariant forms of the block.
- *The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra*, for the left multiplication, its adjoint and the operator form of the law.
- *The Specificities of the General Plain Algebra*, for the model article of the construction, where the discriminating law is the left alternativity.
- *Nilpotents of the Antisymmetric Quaternionic Sesqualgebra*, for the recurrence and the index that the law governs.
- *Idempotents of the Antisymmetric Quaternionic Sesqualgebra* and *Norm and Invertibility in the Antisymmetric Quaternionic Sesqualgebra*, for the two deliveries on the diagonal.
- *Square Roots of Minus One, Zero and Plus One in the Antisymmetric Quaternionic Sesqualgebra*, for the emptiness of the roots of the nonzero central values.
- *The 12 Products of the Biquaternion Complex Space* and *The 12 Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, for the twelve products read as the structures they define.
