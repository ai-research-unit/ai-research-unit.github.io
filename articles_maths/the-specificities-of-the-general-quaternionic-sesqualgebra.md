# __The Specificities of the General Quaternionic Sesqualgebra__

## Introduction

The general quaternionic sesquilinear product

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*}
$$

is the fourth of the four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space*, and it is the least classical of them: it has no unit, no centre, no associativity, and its element classes are the ones of *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*, *Zero Divisors of the General Quaternionic Sesqualgebra* and *Square Roots of a General Element in the General Quaternionic Sesqualgebra*. As an **operator-theoretic** object it is poorer still: the left multiplication is conjugate-linear, the right multiplication is linear, the composite of two left multiplications is the linear sandwich, and the parity obstruction excludes projectors and square-zero operators in both families altogether.

The reason the block is separated from the other eleven structures is a single law. The two actions of the central element $e_0$ are the natural conjugation on the right and the star on the left,

$$
\tilde P\star e_0 = \tilde P^{\natural} , \qquad e_0\star\tilde Q = \tilde Q^{*} ,
$$

and the identity that collects them is the **star identity**

$$
\bigl(\tilde P\star\tilde Q\bigr)^{*} = \tilde Q\,\overline{\tilde P} ,
$$

equivalently the factorization $\tilde P\star\tilde Q = (\overline{\tilde Q}\tilde P)^{\natural}$. The block is the only one of the twelve structures satisfying it, and it is the identity, and not the pair of actions, that is the law: the two actions are a consequence of the identity, while the symmetrisation $\mathrm{SQS}$ shares them and fails the identity. The article states the identity as the criterion, proves it, and isolates the block among the twelve. It then collects the consequences, which are the specificities of the block: the parities of the two slots (linear in the first, conjugate-linear in the second), the absence of projectors and of square-zero operators, the square and the Krein form, the idempotents which are units of the plain algebra, and the failure of the Jordan triple identity.

**Placement.** The article is the fifth entry, and the synthesis, of the *Specific Theory* section of the general quaternionic sesqualgebra, after *The Two One-Sided Actions and the Absence of a Unit*, *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, *The Associator of the General Quaternionic Sesquilinear Product* and *The Ternary Product and the Failure of the Jordan Triple Identity*. Its twins are *The Specificities of the General Plain Algebra*, which states the left-alternativity criterion of the plain product, and *The Specificities of the General Quaternionic Algebra*, which states the isotope criterion of the natural product; the three criteria are the three ways in which one of the four general products can be singled out.

**Conventions.** $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0 = 1, e_1, e_2, e_3$ with $e_1e_2 = e_3$ and central scalar imaginary $i$. Juxtaposition is the **plain** product, $\star$ is the general quaternionic sesquilinear product $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$, the natural conjugation ${}^{\natural}$ lying in the first slot and the star ${}^{*}$ in the second, and the subscript of an operator is the element it is indexed by. The natural conjugation is ${}^{\natural}$, $\tilde Q^{\natural} = Q_0-\vec Q$; the star is ${}^{*}$, $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$; and $\overline{\tilde Q} = \tilde Q^{\natural*} = \tilde Q^{*\natural}$ is the Hermitian conjugation; all three fix $e_0$. The **central square** is $C(\tilde Q) = \sum_\mu Q_\mu^2$ with $C(\tilde Q)e_0 = \tilde Q\tilde Q^{\natural}$; the **sandwich** of the pair $(A,B)$ is the map $\tilde X\mapsto A\tilde X B$ of the plain product.

## The Law

**Theorem (the criterion).** Among the twelve structures on the biquaternion space the general quaternionic sesquilinear product is the unique one satisfying the **star identity**

$$
\bigl(\tilde P\star\tilde Q\bigr)^{*} = \tilde Q\,\overline{\tilde P}
$$

for all $\tilde P,\tilde Q$, equivalently the unique one that factors as

$$
\tilde P\star\tilde Q = \bigl(\overline{\tilde Q}\,\tilde P\bigr)^{\natural} .
$$

**Proof.** *The block satisfies the law.* The identity $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ and the relation $\tilde Q^{*} = \overline{\tilde Q^{\natural}}$ give $\tilde P\star\tilde Q = \tilde P^{\natural}\overline{\tilde Q^{\natural}}$, and ${}^{\natural}$ is an anti-automorphism of the plain product, so $\tilde P^{\natural}\overline{\tilde Q^{\natural}} = (\overline{\tilde Q}\tilde P)^{\natural}$, since $\natural(\overline{\tilde Q}) = \overline{\tilde Q^{\natural}}$. That is the factorization. Applying ${}^{*}$ to it, and using that ${}^{*}$ is an anti-automorphism of the plain product fixing $e_0$, gives $(\tilde P\star\tilde Q)^{*} = ((\overline{\tilde Q}\tilde P)^{\natural})^{*} = (\overline{\tilde Q}\tilde P)^{\natural*} = \overline{\overline{\tilde Q}\tilde P} = \overline{\overline{\tilde Q}}\,\bar P = \tilde Q\bar P$, the star identity. At $\tilde Q = e_0$ it gives $(\tilde P\star e_0)^{*} = \bar P$, that is $\tilde P\star e_0 = \bar P^{*} = \tilde P^{\natural}$; at $\tilde P = e_0$ it gives $(e_0\star\tilde Q)^{*} = \tilde Q$, that is $e_0\star\tilde Q = \tilde Q^{*}$. So the two actions are the stated ones.

*The identity forces the block.* Conversely, let $\star$ satisfy the star identity. Setting $\tilde Q = e_0$ gives $(\tilde P\star e_0)^{*} = e_0\bar P = \bar P$, hence $\tilde P\star e_0 = \bar P^{*} = \tilde P^{\natural}$, and setting $\tilde P = e_0$ gives $(e_0\star\tilde Q)^{*} = \tilde Q\bar e_0 = \tilde Q$, hence $e_0\star\tilde Q = \tilde Q^{*}$. So the star identity implies the two actions, and the two actions are therefore **necessary** conditions. They are **not sufficient**: the symmetrisation $\mathrm{SQS}$ of the block, the half-sum $\tfrac12(\tilde P^{\natural}\tilde Q^{*}+\tilde Q^{*}\tilde P^{\natural})$ of *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions*, has the same two actions, and the identity fails at $(\tilde P,\tilde Q) = (e_1,e_2)$, where the left side is the star of $\mathrm{SQS}(e_1,e_2) = 0$, that is $0$, and the right side is $e_2\bar e_1 = -e_3$. The four general products of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* are the case in which a simple reading of the actions settles the identity: they are $\tilde P\star\tilde Q = \theta(\tilde P)\phi(\tilde Q)$ with $\theta\in\{\mathrm{id},{}^{\natural}\}$ in the first slot and $\phi\in\{\mathrm{id},{}^{*}\}$ in the second, the right action $\tilde P\star e_0 = \theta(\tilde P)$ is $\tilde P^{\natural}$ exactly when $\theta = {}^{\natural}$, and the left action $e_0\star\tilde Q = \phi(\tilde Q)$ is $\tilde Q^{*}$ exactly when $\phi = {}^{*}$; among the four the identity selects the product $(\theta,\phi) = ({}^{\natural},{}^{*})$, which is the block. The eight derived parts are not of that form, and for them the identity is tested directly in the section below, where every structure other than the block is given a basis pair at which the two sides differ.

## The Isolation among the Twelve

The test is the **star identity** $(\tilde P\star\tilde Q)^{*}=\tilde Q\overline{\tilde P}$. The eight derived parts are the symmetric and antisymmetric parts of the four general products (*The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*), and the four general products are the readings $\tilde P\star\tilde Q=\theta(\tilde P)\phi(\tilde Q)$ with $\theta\in\{\mathrm{id},{}^{\natural}\}$ in the first slot and $\phi\in\{\mathrm{id},{}^{*}\}$ in the second.

**Theorem (the isolation).** Of the twelve structures of *The Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, the block is the only one satisfying the star identity.

*Proof.* The four general products are settled by their slots: the right action $\tilde P\star e_0=\theta(\tilde P)$ is $\tilde P^{\natural}$ exactly when $\theta={}^{\natural}$, and the left action $e_0\star\tilde Q=\phi(\tilde Q)$ is $\tilde Q^{*}$ exactly when $\phi={}^{*}$; the two actions are necessary for the identity, and among the four general products they select the block alone. The eight derived parts are not of that form, and each fails the identity on a basis pair: the symmetric part SPA and the three other general products give $-e_1$ at $(e_0,e_1)$ or $(e_1,e_0)$ where $e_1$ is required; the four antisymmetrisations APA, AQA, APS and AQS vanish at the pair of units $(e_0,e_0)$ where $e_0$ is required; SQA and SPS vanish at $(e_0,e_1)$ where $e_1$ is required; and the symmetrisation SQS of the block, the only one that survives the pair of units, is removed by the vector pair $(e_1,e_2)$, where its value vanishes and the right side is $-e_3$.

| the failure of the star identity | the structures |
|---|---|
| $-e_1$ at $(e_0,e_1)$, $e_1$ required | GPA, GQA, SPA |
| $-e_1$ at $(e_1,e_0)$, $e_1$ required | GPS |
| $0$ at $(e_0,e_0)$, $e_0$ required | APA, AQA, APS, AQS |
| $0$ at $(e_0,e_1)$, $e_1$ required | SQA, SPS |
| $0$ at $(e_1,e_2)$, $-e_3$ required | SQS |
| **equal at every pair** | **GQS** |

The block is the only row whose two entries agree, and the criterion is proved. The symmetrisation SQS is the nearest structure: it shares the two actions of $e_0$ with the block and fails the identity, which is why the law is the identity and not the pair of actions.

## The Parities of the Slots and the Absence of Projectors

**Theorem (the parities of the two slots).** The block is $\mathbb{C}$-**linear in the first slot** and **conjugate-linear in the second**:

$$
(\lambda\tilde P)\star\tilde Q = \lambda\,\tilde P\star\tilde Q , \qquad \tilde P\star(\lambda\tilde Q) = \overline{\lambda}\,\tilde P\star\tilde Q , \qquad \lambda\in\mathbb{C} .
$$

It is one of the two sesquilinear products of the four *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*; at the operator level its left multiplication is conjugate-linear and its right multiplication is **linear**.

**Proof.** $\tilde P\star(\lambda\tilde Q) = \tilde P^{\natural}(\lambda\tilde Q)^{*} = \tilde P^{\natural}\overline{\lambda}\tilde Q^{*} = \overline{\lambda}\tilde P\star\tilde Q$, while $(\lambda\tilde P)\star\tilde Q = (\lambda\tilde P)^{\natural}\tilde Q^{*} = \lambda\tilde P^{\natural}\tilde Q^{*} = \lambda\tilde P\star\tilde Q$, the natural conjugation being $\mathbb{C}$-linear. Among the four general products, $\tilde P\tilde Q$ and $\tilde P^{\natural}\tilde Q$ are $\mathbb{C}$-bilinear, the general plain sesquilinear product $\tilde P\tilde Q^{*}$ is linear in the first slot and conjugate-linear in the second, and the block is the same type, with the natural conjugation inserted in the first slot; the block is therefore **not** the unique sesquilinear one, the distinction from its sibling being the first slot. This is the row of the definition of the sesquilinear multiplication in *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*.

**Theorem (the left multiplication, and its square).** The left multiplication of the block is

$$
L_{\tilde P}(\tilde X) = \tilde P^{\natural}\tilde X^{*} ,
$$

it is conjugate-linear, and the composite of two of them is the **linear** sandwich

$$
L_{\tilde P}L_{\tilde R}(\tilde X) = \tilde P^{\natural}\,\tilde X\,\overline{\tilde R} .
$$

**Proof.** The first display is the definition of the product read as an operator identity. For the second, $L_{\tilde P}L_{\tilde R}(\tilde X) = \tilde P^{\natural}\bigl(\tilde R^{\natural}\tilde X^{*}\bigr)^{*}$, and ${}^{*}$ is an anti-automorphism of the plain product with $(\tilde X^{*})^{*} = \tilde X$, $(\tilde R^{\natural})^{*} = \tilde R^{\natural*} = \overline{\tilde R}$ and $(\tilde Z^{*})^{*}=\tilde Z$, so the bracket is $\tilde X\overline{\tilde R}$ and the composite is $\tilde P^{\natural}\tilde X\overline{\tilde R}$. The composite is linear in $\tilde X$ while each factor is conjugate-linear, which is the parity shift: the product of two conjugate-linear maps is linear, so the family of left multiplications is not stable under composition and is not a monoid. The maps and the sandwich are computed in *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*.

**Corollary (no projector, no square-zero operator).** The block has no projector and no square-zero operator in either family: there is no $\tilde P\neq0$ with $L_{\tilde P}^{2} = L_{\tilde P}$ or with $L_{\tilde P}^{2} = 0$, and none with $R_{\tilde P}^{2} = R_{\tilde P}$ or with $R_{\tilde P}^{2} = 0$.

**Proof.** A conjugate-linear map $L$ on a complex space satisfies $L(\lambda\tilde X) = \overline{\lambda}L(\tilde X)$ for every $\lambda$, so $L^{2}$ is linear, $L^{2}(\lambda\tilde X) = \lambda L^{2}(\tilde X)$. If $L_{\tilde P}^{2} = L_{\tilde P}$ and $L_{\tilde P}\neq0$ then $L_{\tilde P}$ would be both conjugate-linear and linear, forcing $L_{\tilde P} = 0$, a contradiction; and $L_{\tilde P}^{2}(\tilde X) = \tilde P^{\natural}\tilde X\overline{\tilde P}$ is a sandwich of the simple ring $\mathbb{B}$, which vanishes identically only when $\tilde P = 0$. For the right family, $R_{\tilde P}(\tilde X)=\tilde X^{\natural}\tilde P^{*}$ is $\mathbb{C}$-linear, with square $R_{\tilde P}^{2}(\tilde X) = \overline{\tilde P}\,\tilde X\,\tilde P^{*}$. If $R_{\tilde P}^{2} = 0$ then the sandwich $\overline{\tilde P}(\cdot)\tilde P^{*}$ vanishes identically, so one of $\overline{\tilde P}$, $\tilde P^{*}$ is zero, that is $\tilde P = 0$. If $R_{\tilde P}^{2} = R_{\tilde P}$ then, at $\tilde X = e_0$ and with $c = \tilde P^{*}$, one gets $c^{\natural}c = c$; the left side is the central square $\bigl(\sum_\mu c_\mu^{2}\bigr)e_0$, so $c$ has no vector part and its scalar coordinate satisfies $c_0^{2} = c_0$, giving $c = 0$ or $c = e_0$; the first is $\tilde P = 0$, and the second is $\tilde P = e_0$, for which the right multiplication is the natural conjugation, $R_{e_0}(\tilde X) = \tilde X^{\natural}$, whose square is the identity and not itself. The parity argument for the left family is the one of *The Specificities of the General Plain Algebra*, where it excludes the projectors of the four sesquilinear structures.

This is the operator-theoretic specificity of the block, and it is the exact opposite of the plain product. The plain product is left-alternative and its idempotent elements give projectors; the natural product has a full family of projectors indexed by the plain idempotents, its isotope criterion; the block has no projector and no square-zero operator at all: its left multiplications are conjugate-linear, so the composite moves the parity and the class is not stable, and its right multiplications, though linear, square to plain two-sided multiplications, which can fix or annihilate only the zero parameter. The element theory of the block is as rich as the others and the operator theory is empty.

## The Square, the Idempotents and the Units

**Proposition (the square and the Krein form).** For every $\tilde P$,

$$
\tilde P\star\tilde P = \bigl(\overline{\tilde P}\tilde P\bigr)^{\natural} , \qquad \mathrm{Sc}\bigl(\tilde P\star\tilde P\bigr) = \sum_\mu\varepsilon_\mu\lvert P_\mu\rvert^2 , \qquad \varepsilon = (1,-1,-1,-1) ,
$$

so the scalar part of the square is the **Krein form**, of signature $(2,6)$, and the square of an element is zero exactly on the origin and the family $c(\hat u+i)$ of *Square Roots of Zero and the Nilpotents of the General Quaternionic Sesqualgebra*.

**Proof.** The identity is *The Square of the General Quaternionic Sesquilinear Product and the Two Halves*, the scalar part is the Krein form $K$ of *The Krein Gram Matrix and the Restrictions of the Form*, and the square-zero family is the classification of the cited article.

**Theorem (the nontrivial idempotents are units of the plain algebra).** The nontrivial idempotents of the block are the elements

$$
\tilde\Pi = -\tfrac12e_0+\vec n , \qquad \vec n = n_1e_1+n_2e_2+n_3e_3 , \qquad \sum_{k=1}^{3}n_k^2 = \tfrac34 ,
$$

and every one of them has central square $C(\tilde\Pi) = 1$; so the nontrivial idempotents of the block are **units of the plain algebra**, and the block has no unit in which they could be units of the block.

**Proof.** The parametrization is *Square Roots of One and the Idempotents of the General Quaternionic Sesqualgebra*, where the idempotent equation $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ is reduced to the equation on $\vec n$; the central square of $-\tfrac12e_0+\vec n$ is $\tfrac14+\sum_kn_k^2 = \tfrac14+\tfrac34 = 1$. The block has no unit by *The Two One-Sided Actions and the Absence of a Unit*, so the invertibility of the idempotents is the invertibility of the plain algebra.

The corollary is the second specificity: the **nontrivial** idempotents of the block are the only nontrivial idempotents among the four general products that are units of the plain algebra, the trivial idempotent $e_0$ being a unit for all four. The nontrivial idempotents of the plain product and of the general plain sesquilinear product have vanishing central square and are zero divisors, and the natural product has no nontrivial idempotent at all, so the family $-\tfrac12e_0+\vec n$ is alone in the unit locus. The block pays for its idempotents with its operator theory, and the comparison is the one of *Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Ternary Product and the Jordan Triple Identity

**Proposition (the ternary product fails).** The ternary product of the block,

$$
\{P,Q,R\} = (P\star Q)\star R^{*} = \overline{Q}\,P\,R ,
$$

does not satisfy the Jordan triple identity

$$
\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\}
$$

of the theory of algebraic $J^{*}$-algebras. At the basis elements $(x,y,u,v,w) = (e_0,e_1,e_0,e_2,e_0)$ the two sides are $e_3$ and $-3e_3$, which differ.

**Proof.** The ternary product is read from the factorization: $(P\star Q)\star R^{*} = (P\star Q)^{\natural}(R^{*})^{*} = \overline{Q}PR$, the plain triple product with the first factor conjugated, because $(P\star Q)^{\natural} = \overline{Q}P$. The two sides at the quintuple are computed in *The Ternary Product and the Failure of the Jordan Triple Identity*, where the identity is tested on the basis and the count is recorded; the source of the failure is the first slot's natural conjugation, as the reading of §*The First Slot Is the Source* of *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* shows.

So the block fails even the algebraic identity that the other sesquilinear structures satisfy, and it fails it at a basis quintuple. The failure is not an accident of the product: it is the same first-slot conjugation that gives the criterion of §*The Law* and the Krein form of §*The Square, the Idempotents and the Units*.

## What the Algebra Is Not

The three losses are the reason the block is separated, and they have one source, the conjugation in the first slot.

- **No unit, no centre, no invertibility.** The right action of $e_0$ is the natural conjugation and the left action is the star, so there is no two-sided unit, no inverse, and no invertible element; the centre is trivial. The absence is *The Two One-Sided Actions and the Absence of a Unit* and *Norm and Invertibility in the General Quaternionic Sesqualgebra*.
- **No associativity, no alternativity, no flexibility, no power associativity.** The witnesses are in *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* and *The Associator of the General Quaternionic Sesquilinear Product*; the product is symmetric neither in the slots nor under the reversal of the factors.
- **No projector, no square-zero operator, no monoid of left multiplications.** The left multiplications are conjugate-linear, their composites are the linear sandwiches, the right multiplications are linear, and the parity obstruction removes the projectors and the square-zero operators of both families. The operator-level reading is *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, and the sandwich $A^{\natural}(\cdot)\overline{B}$ is the composite of two left multiplications.

## Summary

The general quaternionic sesquilinear product $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ is the unique one of the twelve structures on the biquaternion space satisfying the star identity $(\tilde P\star\tilde Q)^{*} = \tilde Q\overline{\tilde P}$, equivalently the unique one that factors as $\tilde P\star\tilde Q = (\overline{\tilde Q}\tilde P)^{\natural}$. Its two actions of $e_0$ follow by specialization, $\tilde P\star e_0 = \tilde P^{\natural}$ and $e_0\star\tilde Q = \tilde Q^{*}$, and they are necessary conditions only: the symmetrisation $\mathrm{SQS}$ shares them and fails the identity. The isolation exhibits, for each of the other structures, a basis pair at which the two sides differ, and the four general products are settled among themselves by the two actions.

The consequences are the specificities of the block. The product is linear in the first slot and conjugate-linear in the second, the left multiplication is $L_{\tilde P}(\tilde X) = \tilde P^{\natural}\tilde X^{*}$ with composite the linear sandwich $L_{\tilde P}L_{\tilde R}(\tilde X) = \tilde P^{\natural}\tilde X\overline{\tilde R}$, the right multiplication $R_{\tilde P}(\tilde X) = \tilde X^{\natural}\tilde P^{*}$ is linear, and the parity obstruction removes every projector and every square-zero operator, in contrast to the plain and the natural products. The square is the natural conjugate of the plain product, its scalar part is the Krein form of signature $(2,6)$, and its vanishing cuts out, beyond the origin, the family $c(\hat u+i)$ in the non-pure part of the cone. The nontrivial idempotents are the family $-\tfrac12e_0+\vec n$ with $\sum_kn_k^2 = \tfrac34$, and they are units of the plain algebra while the block has no unit. The ternary product fails the Jordan triple identity at a basis quintuple, and the first-slot conjugation is the common source of the criterion, the sign vector of the scalar form, the absence of a unit and the failure of the identity. The block has the element theory of the sesquilinear structures and none of their operator theory.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ | the general quaternionic sesquilinear product, the block |
| $\tilde P\star e_0 = \tilde P^{\natural}$, $e_0\star\tilde Q = \tilde Q^{*}$ | the two actions of $e_0$, a consequence of the identity and not sufficient alone |
| $(\tilde P\star\tilde Q)^{*} = \tilde Q\overline{\tilde P}$ | the star identity, the criterion |
| $\tilde P\star\tilde Q = (\overline{\tilde Q}\tilde P)^{\natural}$ | the factorization, equivalent to the criterion |
| $L_{\tilde P}(\tilde X) = \tilde P^{\natural}\tilde X^{*}$ | the conjugate-linear left multiplication |
| $R_{\tilde P}(\tilde X) = \tilde X^{\natural}\tilde P^{*}$ | the linear right multiplication |
| $L_{\tilde P}L_{\tilde R}(\tilde X) = \tilde P^{\natural}\tilde X\overline{\tilde R}$ | the linear sandwich of the composite |
| $C(\tilde Q) = \sum_\mu Q_\mu^2$ | the central square, the norm of the plain algebra |
| $\tilde\Pi = -\tfrac12e_0+\vec n$, $\sum_kn_k^2 = \tfrac34$ | the nontrivial idempotents, units of the plain algebra |
| $\{P,Q,R\} = \overline{Q}PR$ | the ternary product |

## Further Reading

- *The Specificities of the General Plain Algebra* (`articles_maths/the-specificities-of-the-general-plain-algebra.md`), for the left-alternativity criterion and the parity obstruction, the twin of the present article.
- *The Specificities of the General Quaternionic Algebra* (`articles_maths/the-specificities-of-the-general-quaternionic-algebra.md`), for the isotope criterion of the natural product.
- *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the product, its table, the first-slot reading of the scalar form and the failure of the ternary identity.
- *Introduction to the Symmetric Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-sesqualgebra-of-biquaternions.md`), for the symmetrisation $\mathrm{SQS}$, which shares the two actions of $e_0$ and fails the star identity, and for the sibling $\mathrm{SPS}$.
- *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.md`), for the adapted exchange that constructs the eight derived parts.
- *The Two One-Sided Actions and the Absence of a Unit* (`articles_maths/the-two-one-sided-actions-and-the-absence-of-a-unit.md`), for the two actions of $e_0$ and the absence of a unit.
- *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product* (`articles_maths/the-left-and-right-multiplications-of-the-quaternionic-sesquilinear-product.md`), for the left and right multiplications and the sandwich.
- *The Associator of the General Quaternionic Sesquilinear Product* (`articles_maths/the-associator-of-the-quaternionic-sesquilinear-product.md`), for the associator and the failure of the associativity laws.
- *The Ternary Product and the Failure of the Jordan Triple Identity* (`articles_maths/the-ternary-product-and-the-failure-of-the-jordan-triple-identity.md`), for the ternary product and the quintuple witness.
- *The Four General Products of the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-four-general-products-of-the-biquaternion-c-space.md`), for the definition of the four products and the two slot involutions.
- *The Square of the General Quaternionic Sesquilinear Product and the Two Halves* (`articles_maths/the-square-of-the-quaternionic-sesquilinear-product-and-the-two-halves.md`), for the square and the Krein form.
- *Conventions in Mathematics* (`articles_maths/conventions-in-mathematics.md`), for the notation and the article format.
