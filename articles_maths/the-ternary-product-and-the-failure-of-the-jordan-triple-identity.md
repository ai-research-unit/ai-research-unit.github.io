
# __The Ternary Product and the Failure of the Jordan Triple Identity__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ carries four general products on its underlying $\mathbb{C}$-vector space (*The Four General Products of the Biquaternion $\mathbb{C}$ Space*), and the fourth of them,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

is the subject of this group. The rule and the scalar–vector form are *The Four General Products of the Biquaternion $\mathbb{C}$ Space* §*The General Quaternionic Sesquilinear Product*; the sesqualgebra it defines, its two actions of the unit and its associator are *Introduction to the General Quaternionic Sesqualgebra of Biquaternions*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation $\tilde P^{\natural} = P_0 - \mathbf P$, ${}^{*}$ is the star conjugation $\tilde P^{*} = \overline{P_0} - \overline{\mathbf Q}$, and the bar is the coefficientwise complex conjugation.

The subject of this article is the **ternary product** attached to the multiplication and the failure of the **Jordan triple identity** for it. The binary multiplication has no unit (*The Two One-Sided Actions and the Absence of a Unit*) and is not associative (*The Associator of the General Quaternionic Sesquilinear Product*), and the ternary product is the natural replacement: it is the three-slot operation

$$
\{\tilde P,\tilde Q,\tilde R\} = (\tilde P \star \tilde Q) \star \tilde R^{*} = \overline{\tilde Q}\,\tilde P\,\tilde R ,
$$

the general definition $(x,y,z) \mapsto (x \star y) \star z^{*}$ of *The Sesquilinear Associator and the Ternary Product* read with this multiplication. The article establishes the following. First, the ternary product is additive in each variable, $\mathbb{C}$-linear in the first and the third and conjugate-linear in the second, and under the relabelling $\tilde Q \mapsto \tilde Q^{\natural}$ it becomes the product $\tilde X^{*}\tilde Y\tilde Z$ of the algebra with its involution, the **left** model of *Algebraic J\*-Algebras*. Second, the Jordan triple identity nevertheless **fails**, the failure being the residue of the missing unit and of the first-slot conjugation, and it fails already on five basis elements. Third, the failure is not repaired on any of the remarkable real subspaces, and it separates this product from the sibling general plain sesquilinear product, whose ternary product is the **middle** model $\tilde X\tilde Y^{*}\tilde Z$ and is a genuine Jordan triple. Fourth, the failure is visible in the operators, where it is the failure of the commutator identity that the Jordan triple identity is equivalent to.

The article owns the ternary product, its parities and the failure of the identity. It cites the general definition and the parity theorem to *The Sesquilinear Associator and the Ternary Product*; it cites the identity and the two models to *Algebraic J\*-Algebras* and the axioms to *Jordan Triples with an Involution*; it cites the operator instance to *The Ternary Product as an Operator*; and it cites the statement of the failure for this product to *Introduction to the General Quaternionic Sesqualgebra of Biquaternions* §*The Ternary Product* and §*The Failure of the Jordan Triple Identity*, whose proofs it expands and whose witness it re-reads. Four auxiliary statements support the failure: the coordinate form, which presents the ternary product as the plain product of the conjugated middle factor with the outer two; the relation to the associator, which identifies the first term of the associator as the ternary product at the third argument $\tilde R^{*}$; the operator form, in which the identity becomes a commutator identity for the linear operators $\Theta_{\tilde P,\tilde Q}$; and the restriction to the remarkable subspaces, on which the failure survives.

## The Ternary Product

### Definition

**Definition.** The **ternary product** attached to the multiplication is

$$
\{\tilde P,\tilde Q,\tilde R\} = (\tilde P \star \tilde Q) \star \tilde R^{*} , \qquad \tilde P,\tilde Q,\tilde R \in \mathbb{B} .
$$

The general definition of *The Sesquilinear Associator and the Ternary Product* is $(x,y,z) \mapsto (x \star y) \star z^{*}$ for a multiplication $\star$ and an involution ${}^{*}$; the definition above is that general one read with the multiplication of this group.

**Proposition (the closed form).** For all biquaternions $\tilde P, \tilde Q, \tilde R$,

$$
\{\tilde P,\tilde Q,\tilde R\} = \overline{\tilde Q}\,\tilde P\,\tilde R ,
$$

the product on the right being the plain product of the algebra.

**Proof.** Expanding the outer multiplication, $(\tilde P \star \tilde Q) \star \tilde R^{*} = (\tilde P^{\natural}\tilde Q^{*})^{\natural}(\tilde R^{*})^{*}$. The first factor is $(\tilde Q^{*})^{\natural}(\tilde P^{\natural})^{\natural} = \overline{\tilde Q}\,\tilde P$ by the anti-multiplicativity of ${}^{\natural}$ and the identity $(\tilde X^{*})^{\natural} = \overline{\tilde X}$; the second factor is $(\tilde R^{*})^{*} = \tilde R$. Multiplying gives the closed form. $\square$

**Remark.** The closed form shows that the ternary product is the plain product of the three *conjugated* factors $\overline{\tilde Q}$, $\tilde P$ and $\tilde R$, and it is the ternary analogue of the associator formula $\overline{\tilde Q}\tilde P\tilde R^{*} - \tilde P^{\natural}\tilde R\overline{\tilde Q}$ of *The Associator of the General Quaternionic Sesquilinear Product*: the first term of the associator is the ternary product. The ternary product is the left term of the associator, and the associator is the ternary product minus the second grouping.

### The Parities

**Proposition (parities).** The ternary product is additive in each variable; it is $\mathbb{C}$-linear in the first and the third variables and conjugate-linear in the second,

$$
\{\lambda\tilde P,\tilde Q,\tilde R\} = \lambda\{\tilde P,\tilde Q,\tilde R\} , \qquad \{\tilde P,\lambda\tilde Q,\tilde R\} = \bar\lambda\{\tilde P,\tilde Q,\tilde R\} , \qquad \{\tilde P,\tilde Q,\lambda\tilde R\} = \lambda\{\tilde P,\tilde Q,\tilde R\} .
$$

**Proof.** The plain product is $\mathbb{C}$-bilinear and the conjugation $\overline{\cdot}$ is conjugate-linear, so in the closed form $\overline{\tilde Q}\tilde P\tilde R$ the map is linear in $\tilde P$, conjugate-linear in $\tilde Q$ and linear in $\tilde R$; additivity is the additivity of the plain product and of the conjugation. $\square$

**Remark.** The parities are the parities of a Jordan triple with an involution: a ternary product linear in the two outer slots and conjugate-linear in the middle one is exactly the datum of *Jordan Triples with an Involution* and of the algebraic $J^{*}$-algebras of *Algebraic J\*-Algebras*. The two outer slots are the linear ones and the middle slot is the conjugate-linear one, the opposite arrangement to the multiplication, which is linear in the first slot and conjugate-linear in the second. The ternary product exchanges which of the two "outer" operations of the multiplication is the linear one.

### The Left Model

**Proposition (the left model).** Under the relabelling $\tilde X = \tilde Q^{\natural}$, $\tilde Y = \tilde P$, $\tilde Z = \tilde R$, the ternary product is

$$
\{\tilde P,\tilde Q,\tilde R\} = \tilde X^{*}\,\tilde Y\,\tilde Z ,
$$

the **left model** of *Algebraic J\*-Algebras*, the product of the algebra with its conjugate-linear involution inserted in the first slot.

**Proof.** The relabelling uses $\overline{\tilde Q} = (\tilde Q^{\natural})^{*}$, which is the identity $\overline{\tilde Q} = \tilde Q^{\natural *}$ read on the coordinates; substituting, $\overline{\tilde Q}\tilde P\tilde R = \tilde X^{*}\tilde Y\tilde Z$. $\square$

**Remark.** The **middle model** of the same theory is $\tilde X\tilde Y^{*}\tilde Z$, with the involution in the middle slot. The ternary product of the sibling general plain sesquilinear product $\tilde P\tilde Q^{*}$ is the middle model, since there $(\tilde P\star_s\tilde Q)\star_s\tilde R^{*} = (\tilde P\tilde Q^{*})(\tilde R^{*})^{*} = \tilde P\tilde Q^{*}\tilde R$, the middle model with the involution on the second factor. The two models are the same formula with the involution in the first or the middle slot, and this is the transposition that the group article isolates: the multiplication of this group carries the $\mathbb{C}$-linear insertion ${}^{\natural}$ in its first slot, which passes to the ternary product as the first-slot involution and moves the ternary product from the middle to the left model. The difference is not cosmetic, because the theory of *Algebraic J\*-Algebras* is built for the middle model and its identity is not preserved by the transposition, as the next section proves.

### Additivity and the Operator

**Proposition (the operator of a pair).** For fixed $\tilde P$ and $\tilde Q$, the map $\Theta_{\tilde P,\tilde Q} : \tilde R \mapsto \{\tilde P,\tilde Q,\tilde R\}$ is $\mathbb{C}$-linear, and it is the plain left multiplication

$$
\Theta_{\tilde P,\tilde Q} = T_{\overline{\tilde Q}\tilde P,\,e_0} , \qquad \Theta_{\tilde P,\tilde Q}(\tilde R) = \bigl(\overline{\tilde Q}\,\tilde P\bigr)\tilde R ,
$$

the operator attached to the pair $(\tilde P,\tilde Q)$ in the sense of *The Ternary Product as an Operator*. The pair map $(\tilde P,\tilde Q)\mapsto\Theta_{\tilde P,\tilde Q}$ is $\mathbb{C}$-linear in $\tilde P$ and conjugate-linear in $\tilde Q$.

**Proof.** The variable $\tilde R$ enters through the plain product on the right, so $\Theta_{\tilde P,\tilde Q}(\lambda\tilde R+\mu\tilde R')=\lambda\Theta_{\tilde P,\tilde Q}(\tilde R)+\mu\Theta_{\tilde P,\tilde Q}(\tilde R')$; the factorisation through the plain left multiplication by $\overline{\tilde Q}\tilde P$ is the closed form $\overline{\tilde Q}\tilde P\tilde R$. The parities of the pair map are those of the closed form in the first two arguments. $\square$

**Remark.** The operator is a plain left multiplication, a $\mathbb{C}$-linear endomorphism of $\mathbb{B}$, and this agrees with the third reading of *The Ternary Product as an Operator* §*The Three Readings*: the third slot of the ternary product gives a plain one-sided operator. What the pair map carries of the ternary structure is its parity, conjugate-linear in the second argument, and this is the same conjugate-linearity that the middle-slot reading of that article names as the sandwich $S_{\tilde P,\tilde R} : \tilde Q\mapsto\tilde P\tilde Q^{*}\tilde R$, which in the closed form is $\overline{\tilde Q}\tilde P\tilde R$ with the conjugation moved. The middle-slot reading is the only conjugate-linear reading of the three, and it is the one the Jordan triple identity tests.

### The Coordinate Form

**Proposition (the coordinate form).** For all biquaternions $\tilde P,\tilde Q,\tilde R$,

$$
\{\tilde P,\tilde Q,\tilde R\} = \overline{\tilde Q}\,\bigl(\tilde P\tilde R\bigr) = \bigl(\overline{\tilde Q}\tilde P\bigr)\tilde R ,
$$

the plain product being associative, and the scalar part is

$$
\mathrm{Sc}\{\tilde P,\tilde Q,\tilde R\} = \overline{Q_0}\,\mathrm{Sc}\bigl(\tilde P\tilde R\bigr) - \bigl(\overline{\mathbf Q},\mathrm{Vec}(\tilde P\tilde R)\bigr) ,
$$

with $\mathrm{Sc}(\tilde P\tilde R) = P_0R_0 - (\mathbf P,\mathbf R)$ and $\mathrm{Vec}(\tilde P\tilde R) = P_0\mathbf R + R_0\mathbf P + \mathbf P\times\mathbf R$.

**Proof.** The closed form is $\overline{\tilde Q}\tilde P\tilde R$; the plain product is associative, so the two groupings written agree, and this is the only regrouping the associativity of the algebra offers. The scalar part is the scalar part of the plain product of $\overline{\tilde Q}$ and $\tilde P\tilde R$, that is $\overline{Q_0}\mathrm{Sc}(\tilde P\tilde R) - (\overline{\mathbf Q},\mathrm{Vec}(\tilde P\tilde R))$ by the scalar–vector rule of the plain product; the two displayed values are that rule read on $\tilde P\tilde R$. $\square$

**Corollary (the degenerate cases on the identity).** With $\tilde Q = e_0$ the ternary product is the plain product of the outer factors, $\{\tilde P,e_0,\tilde R\} = \tilde P\tilde R$; with $\tilde R = e_0$ it is $\{\tilde P,\tilde Q,e_0\} = \overline{\tilde Q}\tilde P$; and with $\tilde P = e_0$ it is $\{e_0,\tilde Q,\tilde R\} = \overline{\tilde Q}\tilde R$.

**Proof.** Each is the closed form with the indicated argument the identity and the coefficientwise conjugation of $e_0$ equal to $e_0$. $\square$

**Remark.** The corollary shows that the ternary product contains the plain multiplication: the middle insertion of the identity returns the plain product of the outer factors, $\{\tilde P,e_0,\tilde R\} = \tilde P\tilde R$, so the ternary product determines the multiplication of the algebra, and a fortiori the sesquilinear product, since $\tilde P\star\tilde Q = \tilde P^{\natural}\tilde Q^{*}$ is read from the plain product and the two conjugations. What the ternary product cannot supply is a unit of the sesquilinear multiplication itself: the degenerate values are $\tilde P\tilde R$, $\overline{\tilde Q}\tilde P$ and $\overline{\tilde Q}\tilde R$, and two of the three carry a conjugation, so no insertion of $e_0$ returns an element that is the identity of the twisted product on a side.

### The Ternary Product and the Associator

**Proposition (the associator in ternary terms).** The associator of the multiplication is

$$
[\tilde P,\tilde Q,\tilde R] = (\tilde P\star\tilde Q)\star\tilde R - \tilde P\star(\tilde Q\star\tilde R) = \{\tilde P,\tilde Q,\tilde R^{*}\} - \tilde P^{\natural}\tilde R\,\overline{\tilde Q} ,
$$

so that the first term of the associator is the ternary product evaluated at the third argument $\tilde R^{*}$.

**Proof.** The associator is $\overline{\tilde Q}\tilde P\tilde R^{*} - \tilde P^{\natural}\tilde R\overline{\tilde Q}$ (*The Associator of the General Quaternionic Sesquilinear Product*), and the first term is the closed form with the third argument $\tilde R^{*}$. $\square$

**Corollary (the flexible case).** With $\tilde R = \tilde P$ the associator is $[\tilde P,\tilde Q,\tilde P] = \{\tilde P,\tilde Q,\tilde P^{*}\} - \tilde P^{\natural}\tilde P\overline{\tilde Q}$; the flexible law would require this to vanish for all $\tilde P$ and $\tilde Q$, and it does not.

**Proof.** Substituting $\tilde R = \tilde P$ in the display. The failure is *The Associator of the General Quaternionic Sesquilinear Product*, §*The Failure of the Weaker Laws*, which exhibits the triples. $\square$

**Remark.** The association that the ternary product cannot see is the one in which the middle factor is conjugated after the product: the associator is nonzero exactly because the ternary product conjugates the middle factor before multiplying it, and the second grouping conjugates it after. In the sibling sesquilinear product the involution and the product commute well enough for the two terms to cancel in the middle model, and this is why the sibling's associator is the one that carries the identity.

### Worked Cases

**Example.** On the basis elements the closed form computes a handful of values directly:

| triple | value | reason |
|---|---|---|
| $\{e_1,e_2,e_3\}$ | $e_0$ | $e_2e_1e_3 = (-e_3)e_3 = e_0$ |
| $\{e_1,e_1,e_1\}$ | $-e_1$ | $e_1e_1e_1 = -e_1$ |
| $\{e_1,e_2,e_1\}$ | $-e_2$ | $e_2e_1e_1 = -e_2$ |
| $\{ie_1,ie_2,e_0\}$ | $-e_3$ | $(-ie_2)(ie_1) = e_2e_1 = -e_3$ |

The fourth row shows the coefficientwise conjugation acting on the middle factor: the conjugation of $ie_2$ is $-ie_2$, and it is this and not the multiplication that produces the value.

**Example (the conjugate-linearity in the middle slot).** With the same outer arguments and one inner argument scaled by $i$,

$$
\{e_0,e_1,ie_2\} = i\{e_0,e_1,e_2\} = ie_3 , \qquad \{e_0,ie_1,e_2\} = \bar i\,\{e_0,e_1,e_2\} = -ie_3 ,
$$

so the scaling of the middle argument by $i$ multiplies the value by the conjugate scalar $\bar i = -i$, while the scaling of the third argument by $i$ multiplies it by $i$: the middle slot is conjugate-linear, the outer slots are linear, and the two rules are visible on this pair of triples.

**Remark.** The examples fix the sign conventions of the group: the two conjugations enter the closed form as a conjugation of the middle factor and the plain product of the three factors in the order middle, first, third, and the middle slot is the conjugate-linear one. The remaining article of the group, *The Left and Right Multiplications of the General Quaternionic Sesquilinear Product*, is the operator form of the binary product and not of the ternary one, so these examples are the ones the batch uses when it needs a numerical triple.

## The Jordan Triple Identity

### The Identity

**Definition.** A **Jordan triple** is a module with a ternary product linear in the first and third variables and conjugate-linear in the second, satisfying the **Jordan triple identity**

$$
\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\}
$$

for all $x,y,u,v,w$ (*Jordan Triples with an Involution*). The identity is the linearised form of the defining law of the triple $\{x,y,x\}$, and it is the axiom that makes the operators $\{x,y,\cdot\}$ the generators of a Lie algebra of derivations.

**Remark.** The identity is the ternary counterpart of the Jordan identity, and an algebraic $J^{*}$-algebra is a Jordan triple whose product has the additional algebraic form $\{x,y,z\} = xy^{*}z$ or $x^{*}yz$; the theory of *Algebraic J\*-Algebras* proves the identity for the two models and shows that no identity survives a change of slot that moves the involution out of the middle.

### The Failure

**Theorem (the identity fails).** The ternary product of the multiplication does **not** satisfy the Jordan triple identity. At the basis elements $(x,y,u,v,w) = (e_0,e_1,e_0,e_2,e_0)$ the left-hand side is $e_3$ and the right-hand side is $-3e_3$, so the two differ and the identity fails.

**Proof.** The closed form of the ternary product is $\overline{\tilde Q}\tilde P\tilde R$. The basis coefficients are real, so the coefficientwise conjugation fixes each basis element, $\overline{e_\mu} = e_\mu$.

For the left-hand side, the inner bracket is $\{e_0,e_2,e_0\} = \overline{e_2}e_0e_0 = e_2$, and the outer one is $\{e_0,e_1,e_2\} = \overline{e_1}e_0e_2 = e_1e_2 = e_3$.

For the right-hand side the three terms are as follows. The first is $\{\{e_0,e_1,e_0\},e_2,e_0\}$; the inner bracket is $\{e_0,e_1,e_0\} = \overline{e_1}e_0e_0 = e_1$, and the outer one is $\{e_1,e_2,e_0\} = \overline{e_2}e_1e_0 = e_2e_1 = -e_3$. The second term is $-\{e_0,\{e_1,e_0,e_2\},e_0\}$; the inner bracket is $\{e_1,e_0,e_2\} = \overline{e_0}e_1e_2 = e_1e_2 = e_3$, and the outer one is $\{e_0,e_3,e_0\} = \overline{e_3}e_0e_0 = e_3$, so the term is $-e_3$. The third term is $\{e_0,e_2,\{e_0,e_1,e_0\}\} = \{e_0,e_2,e_1\} = \overline{e_2}e_0e_1 = e_2e_1 = -e_3$. The sum of the three terms is $-e_3 - e_3 - e_3 = -3e_3$, which differs from the left-hand side $e_3$. $\square$

**Remark.** The witness uses only basis elements, and it is the one the group article records. Of the $1024$ five-tuples drawn from the four real quaternion units $e_0,e_1,e_2,e_3$, $480$ make the identity fail and $544$ make it hold; on the full eight-element real basis the same proportion gives $15360$ of the $32768$. The failure is therefore not a small-set phenomenon: the identity is false on an open set of genuine five-tuples and the failure cannot be removed by restricting to the basis. This is the sharp form of the statement that the ternary product has the *parity* of a Jordan triple but not its *identity*.

### The Operator Form of the Failure

**Proposition (the operator form).** Let $\Theta_{\tilde X,\tilde Y}(\tilde R) = \{\tilde X,\tilde Y,\tilde R\}$ be the linear operator of the pair $(\tilde X,\tilde Y)$. The Jordan triple identity is equivalent to the operator identity

$$
[\Theta_{\tilde X,\tilde Y},\Theta_{\tilde U,\tilde V}] = \Theta_{\{\tilde X,\tilde Y,\tilde U\},\tilde V} - \Theta_{\tilde U,\{\tilde Y,\tilde X,\tilde V\}} ,
$$

the bracket being the commutator in $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, and for the multiplication of this group the operator identity fails: at $\tilde X=\tilde U=\tilde W=e_0$, $\tilde Y=e_1$ and $\tilde V=e_2$, the left-hand side applied to $\tilde W$ is $2e_3$ while the right-hand side applied to $\tilde W$ is $-2e_3$.

**Proof.** Expanding the two compositions at an argument $\tilde W$ gives $\Theta_{\tilde X,\tilde Y}\Theta_{\tilde U,\tilde V}(\tilde W) = \{\tilde X,\tilde Y,\{\tilde U,\tilde V,\tilde W\}\}$ and $\Theta_{\tilde U,\tilde V}\Theta_{\tilde X,\tilde Y}(\tilde W) = \{\tilde U,\tilde V,\{\tilde X,\tilde Y,\tilde W\}\}$, so the commutator is the difference of the two sides of the Jordan triple identity after the standard rearrangement, which is the equivalence of *The Ternary Product as an Operator* §*The Bracket and the Lie Triple System*. At the displayed arguments, $\Theta_{\tilde U,\tilde V}(\tilde W) = \{e_0,e_2,e_0\} = e_2$ and $\Theta_{\tilde X,\tilde Y}(\tilde W) = \{e_0,e_1,e_0\} = e_1$, so the left-hand side applied to $\tilde W$ is $\{e_0,e_1,e_2\} - \{e_0,e_2,e_1\} = e_3 - (-e_3) = 2e_3$; and $\{\tilde X,\tilde Y,\tilde U\} = \{e_0,e_1,e_0\} = e_1$ with $\{\tilde Y,\tilde X,\tilde V\} = \{e_1,e_0,e_2\} = e_3$ give the right-hand side applied to $\tilde W$ as $\{e_1,e_2,e_0\} - \{e_0,e_3,e_0\} = -e_3 - e_3 = -2e_3$. $\square$

**Remark.** The operator form is the reason the failure matters: in a Jordan triple the operators $\Theta_{\tilde X,\tilde Y}$ generate a Lie algebra, the first step of the Tits–Kantor–Koecher construction, and the failure of the identity means that this construction is not available for the ternary product of this group. The computation above exhibits the obstruction in the operators themselves: $\Theta_{\tilde P,\tilde Q}$ is the plain left multiplication by $\overline{\tilde Q}\tilde P$, so each $\Theta$ is a left multiplication and the bracket of two of them is the left multiplication by $[\overline{\tilde Y}\tilde X,\overline{\tilde V}\tilde U]$; at the witness this is the left multiplication by $[e_1,e_2]=2e_3$, while the right-hand side is the difference $\Theta_{e_1,e_2}-\Theta_{e_0,e_3}$, the left multiplications by $-e_3$ and by $e_3$, hence the left multiplication by $-2e_3$. The two sides are left multiplications by opposite elements, so the identity fails by the failure of the Jordan triple identity and not by any ambiguity of the operators. The general theory is *Jordan Triples with an Involution* and *Algebraic J\*-Algebras*; the operator statement is *The Ternary Product as an Operator*, and the present article supplies the counterexample that shows the theory's hypothesis is not met.

### The Ternary Product on the Remarkable Subspaces

**Proposition.** On the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the coefficients are real and the coefficientwise conjugation is the identity, the ternary product is the plain product read with the middle argument first,

$$
\{\tilde P,\tilde Q,\tilde R\} = \tilde Q\tilde P\tilde R \qquad (\tilde P,\tilde Q,\tilde R \in \mathbb{H}_{\mathbb{B}}) ,
$$

which is an associative triple product; the Jordan triple identity nevertheless fails there.

**Proof.** For real coefficients $\overline{\tilde Q}=\tilde Q$, so the closed form is $\tilde Q\tilde P\tilde R$. The triple is associative because the plain product is; the failure of the identity on the subspace is the proposition above. $\square$

**Remark.** The proposition isolates the reason the failure is not a failure of associativity of the ternary product: on the quaternion subspace the ternary product is the plain (associative) product with the middle argument in the first position, and the identity still fails. What the middle model $XY^{*}Z$ of *Algebraic J\*-Algebras* requires is the involution in the middle slot together with the argument order of the model; the ternary product of this group inserts a conjugate-linear operation in the middle slot of the multiplication and then conjugates the middle argument of the triple, and it is the argument order, not the associativity, that carries the identity. The same computation shows that no subspace on which the two conjugations agree can repair the failure, since there the product is the plain product with the arguments permuted.

### Where the Identity Still Holds

**Proposition.** The identity holds when all five arguments are central.

**Proof.** For central arguments, $\tilde X = Xe_0$ with $X \in \mathbb{C}$, the ternary product is $\{Xe_0,Ye_0,Ze_0\} = \bar YXZe_0$ by the closed form, and both sides of the Jordan triple identity are complex scalars computed from a commutative product of scalars and their conjugates; the identity reduces to the commutativity and associativity of $\mathbb{C}$, and holds. $\square$

**Remark.** The identity therefore holds on the centre and fails on the whole algebra. The passage from the centre to the algebra is the passage from the commutative base to the non-commutative product, and it is the same passage on which the multiplication first fails associativity.

### The Failure Is Not Repaired on the Real Subspaces

**Proposition.** The identity fails on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where all the coefficients are real and the two sesquilinear products coincide with the two bilinear ones.

**Proof.** The witness $(e_0,e_1,e_0,e_2,e_0)$ already has all its coefficients real, so it is a witness inside $\mathbb{H}_{\mathbb{B}}$; the failure is therefore not a phenomenon of the complex coefficients and survives the restriction to the real quaternion subspace. The identity fails there by the same computation. $\square$

**Remark.** The failure is therefore not a phenomenon of the complex coefficients, and it survives the restriction to every real subspace on which the two conjugations differ: the witness has real coordinates, so it lives in the quaternion subspace and in each of the remarkable subspaces that contains it, and the identity fails there as it fails on the whole algebra. The sibling sesquilinear product, by contrast, is the middle model on the whole algebra and on every subspace, and its identity is not lost by restriction. The failure is recorded by the group article as the reason the general theorems of *Algebraic J\*-Algebras* do not apply to the fourth product's ternary reading.

## The Positive Direction of the Sibling

### The Sibling Sesquilinear Triple Is a Jordan Triple

**Theorem (the sibling).** The ternary product of the sibling general plain sesquilinear product $\tilde P\tilde Q^{*}$ is

$$
(\tilde P,\tilde Q,\tilde R) \mapsto (\tilde P \star_s \tilde Q) \star_s \tilde R^{*} = \tilde P\,\tilde Q^{*}\,\tilde R = \tilde X\tilde Y^{*}\tilde Z ,
$$

under the general definition read with the sibling's multiplication $\star_s$; this is the **middle** model of *Algebraic J\*-Algebras*, and it satisfies the Jordan triple identity.

**Proof.** The general definition gives $(\tilde P\tilde Q^{*})\tilde R^{*}$ with $\star_s$ read as $\tilde X\tilde Y^{*}$; the second factor is $(\tilde R^{*})^{*} = \tilde R$, so the value is $\tilde P\tilde Q^{*}\tilde R$. With $\tilde X = \tilde P$, $\tilde Y = \tilde Q$ and $\tilde Z = \tilde R$ this is the middle model $\tilde X\tilde Y^{*}\tilde Z$, the model for which the identity is proved in *Algebraic J\*-Algebras* from the associativity of the plain product and the involution property of ${}^{*}$; it is a Jordan triple by *Jordan Triples with an Involution*. $\square$

**Remark.** The two ternary products are the two models of the same algebraic $J^{*}$-algebra theory: the sibling's is the middle model and the fourth product's is the left one, and the theory proves the identity for the middle model and not for the left one. The failure of the identity here is therefore not a failure of the sesquilinear kind but the failure of the transposition, and it is the same first-slot insertion that produces the absence of a unit and the failure of flexibility.

### The Two Models and the Transposition

**Corollary.** The two ternary products are related by the conjugations that the isotope inserts,

$$
\{\tilde P,\tilde Q,\tilde R\}_{\text{fourth}} = \{\overline{\tilde Q},\tilde P^{*},\tilde R\}_{\text{sibling}} ,
$$

where the right-hand side is the sibling's ternary product evaluated at the three conjugated arguments.

**Proof.** The sibling's ternary product is $A B^{*} C$ at the arguments $(A,B,C)$. With $A = \overline{\tilde Q}$, $B = \tilde P^{*}$ and $C = \tilde R$, the second factor is $(\tilde P^{*})^{*} = \tilde P$, so the value is $\overline{\tilde Q}\,\tilde P\,\tilde R$, which is the fourth product's ternary product. $\square$

**Remark.** The transposition is a symmetry of the sesquilinearity and not of the theory: the general theory is stated for the middle model, and only that model carries the identity. This is the general phenomenon of *Algebraic J\*-Algebras*, and the fourth product of the biquaternion algebra is its smallest counterexample on a basis: the ternary product of the fourth product is the left model, and it fails the identity at the five basis elements above.

## Summary

The ternary product attached to the general quaternionic sesquilinear multiplication is $\{\tilde P,\tilde Q,\tilde R\} = (\tilde P \star \tilde Q) \star \tilde R^{*} = \overline{\tilde Q}\tilde P\tilde R$, additive in each variable, $\mathbb{C}$-linear in the first and the third and conjugate-linear in the second. The closed form is the plain product of the coefficientwise-conjugated middle factor with the outer two, so it is also $(\overline{\tilde Q}\tilde P)\tilde R$ by the associativity of the plain product, the middle slot carries the conjugation and the outer slots are linear. Under the relabelling $\tilde Q \mapsto \tilde Q^{\natural}$ it is the left model $\tilde X^{*}\tilde Y\tilde Z$ of the theory of algebraic $J^{*}$-algebras, the sibling general plain sesquilinear product giving the middle model $\tilde X\tilde Y^{*}\tilde Z$ instead; the first term of the associator of the multiplication is the ternary product at the third argument $\tilde R^{*}$. The Jordan triple identity $\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\}$ fails for the ternary product of this group: at the basis elements $(e_0,e_1,e_0,e_2,e_0)$ the left-hand side is $e_3$ and the right-hand side is $-3e_3$, so the two differ by $4e_3$, and $480$ of the $1024$ five-tuples of the four real quaternion units are witnesses. The identity holds when all five arguments are central and fails on the quaternion subspace as well as on the whole algebra, so the failure is not an artefact of the complex coefficients. In operator form the identity is the commutator identity $[\Theta_{\tilde X,\tilde Y},\Theta_{\tilde U,\tilde V}] = \Theta_{\{\tilde X,\tilde Y,\tilde U\},\tilde V} - \Theta_{\tilde U,\{\tilde Y,\tilde X,\tilde V\}}$ for the linear operators $\Theta_{\tilde P,\tilde Q}(\tilde R) = \{\tilde P,\tilde Q,\tilde R\}$, which are the plain left multiplications by $\overline{\tilde Q}\tilde P$; at the witness the two sides are the left multiplications by $2e_3$ and by $-2e_3$. The ternary product therefore carries the parity of a Jordan triple and not its identity, and the general theorems of *Algebraic J\*-Algebras* do not apply to it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\{\tilde P,\tilde Q,\tilde R\}$ | the ternary product $(\tilde P\star\tilde Q)\star\tilde R^{*}$ |
| $\{\tilde P,\tilde Q,\tilde R\} = \overline{\tilde Q}\tilde P\tilde R$ | the closed form of the ternary product |
| $\{\tilde P,e_0,\tilde R\} = \tilde P\tilde R$ | the middle identity returns the plain product of the outer factors |
| linear in the first and third, conjugate-linear in the second | the parities of the ternary product |
| $[\tilde P,\tilde Q,\tilde R] = \{\tilde P,\tilde Q,\tilde R^{*}\} - \tilde P^{\natural}\tilde R\overline{\tilde Q}$ | the associator in ternary terms |
| $\tilde X^{*}\tilde Y\tilde Z$ | the left model, the ternary product after the relabelling |
| $\tilde X\tilde Y^{*}\tilde Z$ | the middle model, the sibling sesquilinear ternary product |
| $\Theta_{\tilde P,\tilde Q}(\tilde R) = \{\tilde P,\tilde Q,\tilde R\}$ | the linear operator of a pair, the plain left multiplication by $\overline{\tilde Q}\tilde P$ |
| $[\Theta_{\tilde X,\tilde Y},\Theta_{\tilde U,\tilde V}] = \Theta_{\{\tilde X,\tilde Y,\tilde U\},\tilde V} - \Theta_{\tilde U,\{\tilde Y,\tilde X,\tilde V\}}$ | the operator form of the Jordan triple identity |
| Jordan triple identity | $\{x,y,\{u,v,w\}\} = \{\{x,y,u\},v,w\} - \{u,\{y,x,v\},w\} + \{u,v,\{x,y,w\}\}$ |
| $(e_0,e_1,e_0,e_2,e_0)$ | the basis witness of the failure, $e_3$ against $-3e_3$ |
| $480$ of $1024$ | the five-tuples of the four real quaternion units that witness the failure |

## Further Reading

- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the Jordan triple identity and the passage from the binary to the ternary structure.
- Cho-Ho Chu, *Jordan Structures in Geometry and Analysis* (Cambridge University Press, 2012), for Jordan triples, $J^{*}$-algebras and the two algebraic models.
- Harald Upmeier, *Symmetric Banach Manifolds and Jordan C\*-Algebras* (North-Holland, 1985), for the middle model and the identity that defines it.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the transposition of the involution between the slots of a ternary product.
