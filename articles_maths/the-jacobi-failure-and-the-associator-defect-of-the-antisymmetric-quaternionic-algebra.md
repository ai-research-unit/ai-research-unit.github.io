# __The Jacobi Failure and the Associator Defect of the Antisymmetric Quaternionic Algebra__

## Introduction

The antisymmetric quaternionic multiplication $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ is alternating, vector valued and without a unit, and it fails the Jacobi identity (*Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions*). The failure is one line of the catalogue of the twelve: the witness $(e_0,e_1,e_2)$ with cyclic sum $-e_3$, the block one of the four antisymmetric parts that are not Lie products (*The 12 Products of the Biquaternion Complex Space*). This article does the failure in full. It computes the cyclic sum of the block on general elements, proves that its vanishing is decided on the basis and exhibits the minimal witnesses; it reads the failure through the associator of the parent quaternionic product, using the associator criterion of *The Symmetric and Antisymmetric Parts of an Algebra Product*, and evaluates that criterion on the witness; it isolates the derived bracket, which is a Lie bracket, and shows that the failure is entirely a failure of the scalar-vector interaction; it computes the alternating centre, the annihilator and the elements whose operators commute, all three zero; and it compares the failure with the other two Jacobi failures of the twelve.

The defect is not shared. Of the six symmetrisations and antisymmetrisations of the catalogue, exactly two satisfy the identity of their kind, $\mathrm{APA}$ and $\mathrm{SPA}$, and the four failures have three distinct causes. The block of this article is the one whose cause is **non-associativity alone**: the parent product is not associative, the associator of the quaternionic product is the defect, and the two sesquilinear failures of the catalogue instead come from the obstruction of *Lie Algebras of Sesqualgebras*, in which a genuine sesquilinear slot forbids the collapse of the two involutions that the Jacobi identity would need.

## The Cyclic Sum and Its Closed Form

**Definition.** The **cyclic sum** of the block at the triple $\tilde P,\tilde Q,\tilde R$ is

$$
J(\tilde P,\tilde Q,\tilde R) = (\tilde P\diamond\tilde Q)\diamond\tilde R + (\tilde Q\diamond\tilde R)\diamond\tilde P + (\tilde R\diamond\tilde P)\diamond\tilde Q .
$$

The block satisfies the Jacobi identity exactly when $J$ vanishes identically, and $J$ is the Jacobiator of the operation; it is the cyclic sum declared for the three Jacobi rows of the catalogue.

**Proposition (the closed form).** For all $\tilde P,\tilde Q,\tilde R$,

$$
J(\tilde P,\tilde Q,\tilde R) = -\,P_0\,(\mathbf Q\times\mathbf R) + Q_0\,(\mathbf P\times\mathbf R) - R_0\,(\mathbf P\times\mathbf Q) .
$$

In particular $J(\tilde P,\tilde Q,\tilde R)$ is a pure vector for every triple, the scalar part of every cyclic sum is zero, and $J$ is a $\mathbb{C}$-trilinear alternating map of its three arguments.

*Proof.* Insert the explicit form $\tilde A\diamond\tilde B = A_0\mathbf B-B_0\mathbf A-\mathbf A\times\mathbf B$ into the three terms. The first term is $(\tilde P\diamond\tilde Q)\diamond\tilde R$, whose left factor has scalar part zero and vector part $\mathbf U = P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q$; the term is therefore $0\cdot\mathbf R - R_0\mathbf U - \mathbf U\times\mathbf R = -R_0\mathbf U-\mathbf U\times\mathbf R$, a pure vector. Collecting the three terms the $R_0\mathbf U$ parts give $-R_0\bigl(P_0\mathbf Q-Q_0\mathbf P-\mathbf P\times\mathbf Q\bigr)$ and its two cyclic images, and the cross parts give the three double cross products of $\mathbf U,\mathbf V,\mathbf W$ with $\mathbf R,\mathbf P,\mathbf Q$. The double cross products collapse by the identity $\mathbf U\times(\mathbf A\times\mathbf B) = \mathbf A(\mathbf U,\mathbf B)-\mathbf B(\mathbf U,\mathbf A)$, and the terms with the scalar product of vectors cancel in pairs, leaving the displayed expression; the cancellation is the same one that makes the cyclic sum of the parent product a pure-vector object, and it is carried out monomial by monomial. Alternation follows from the antisymmetry of the cross product: the exchange of two arguments changes the sign of each of the three terms, and the vanishing on a repeated argument is the vanishing of $\mathbf Q\times\mathbf Q$. $\square$

**Proposition (the basis decides).** The cyclic sum is $\mathbb{C}$-trilinear and alternating. It vanishes on all triples exactly when it vanishes on the triples of distinct basis elements, and on the basis it is given by

$$
J(e_\mu,e_\nu,e_\rho)=0 \ \text{ unless } \{\mu,\nu,\rho\}=\{0,j,k\} \ \text{ with } j<k , \qquad
J(e_0,e_j,e_k) = -\,e_j\times e_k .
$$

*Proof.* Trilinearity makes the vanishing on the basis a sufficient condition, by the spanning-set argument of *The Symmetric and Antisymmetric Parts of an Algebra Product* §*Lie-Admissible Algebras*. On the basis, the closed form has one nonzero factor in each term unless the triple is $\{0,j,k\}$: if no argument is $e_0$ the three scalar factors are all zero and the sum is zero, and if a repeated argument occurs the sum is zero by alternation. For the triple $\{0,j,k\}$ the scalar factor of the $e_0$ argument is one and the other two are zero, so the sum is the single term $-e_j\times e_k$, which is nonzero exactly when $j\neq k$. $\square$

The count is therefore three unordered triples, $\{0,1,2\}$, $\{0,1,3\}$ and $\{0,2,3\}$, and eighteen ordered triples out of the sixty-four, since each unordered triple has six orderings and no other triple contributes. The three values are $J(e_0,e_1,e_2)=-e_3$, $J(e_0,e_1,e_3)=e_2$ and $J(e_0,e_2,e_3)=-e_1$, the negatives of the three cross products.

## The Witnesses

**Proposition (the vanishing condition and the minimal witnesses).** The cyclic sum is the closed form, which is $\mathbb{C}$-linear in the triple of scalar parts $(P_0,Q_0,R_0)$ and vanishes identically in them if and only if the three vector parts are pairwise parallel. Otherwise the triples with a vanishing sum are exactly those whose scalar triple lies in the hyperplane

$$
P_0\,(\mathbf Q\times\mathbf R)-Q_0\,(\mathbf P\times\mathbf R)+R_0\,(\mathbf P\times\mathbf Q)=0 ,
$$

and a witness is any triple with one nonzero scalar part and two independent vector parts. The witness of the catalogue is the triple $(e_0,e_1,e_2)$,

$$
J(e_0,e_1,e_2) = (e_0\diamond e_1)\diamond e_2 + (e_1\diamond e_2)\diamond e_0 + (e_2\diamond e_0)\diamond e_1 = e_1\diamond e_2 + (-e_3)\diamond e_0 + (-e_2)\diamond e_1 = -e_3 ,
$$

and the three smallest witnesses are $(e_0,e_1,e_2)$, $(e_0,e_1,e_3)$ and $(e_0,e_2,e_3)$.

*Proof.* In the closed form $J=-P_0(\mathbf Q\times\mathbf R)+Q_0(\mathbf P\times\mathbf R)-R_0(\mathbf P\times\mathbf Q)$ the three coefficients of $P_0,Q_0,R_0$ are the three cross products. A cross product vanishes exactly when its two factors are parallel, so all three coefficients vanish exactly when the three vector parts are pairwise parallel, and then $J=0$ identically in the scalar triple. Otherwise at least one coefficient is nonzero, the solutions of $J=0$ form a hyperplane of the scalar triple, and if one scalar part is nonzero with the vector parts of the other two arguments independent, then the corresponding cross product is nonzero and $J\neq0$. The arithmetic at the witness is the multiplication table of the block. $\square$

The failure is thus a single linear condition on the three scalar parts, and it couples the scalar part to the vector parts. The condition is vacuous exactly when the three vector parts are pairwise parallel; otherwise the safe scalar triples are a hyperplane, so a witness is made of one nonzero scalar part and two independent vector parts. The triples of pure vectors are safe because their scalar triple is zero, and the zero scalar triple always lies in the hyperplane; and a triple with a repeated argument is safe by alternation.

## The Associator Criterion

The block is the antisymmetrisation of the quaternionic product, and the general theory of an antisymmetrised algebra relates its Jacobi identity to the associator of the algebra it came from.

**Theorem (the associator criterion).** Let $A$ be an algebra over a field of characteristic not $2$, $A^{\wedge}$ its antisymmetrisation, $[x,y]=xy-yx$ its commutator and $[x,y,z]=(xy)z-x(yz)$ its associator. Then $A^{\wedge}$ satisfies the Jacobi identity if and only if the associator satisfies the cyclic identity

$$
[x,y,z]+[y,z,x]+[z,x,y] = [y,x,z]+[z,y,x]+[x,z,y] ,
$$

equivalently the Jacobi sum of the commutator is the signed sum of the six associators,

$$
[[x,y],z]+[[y,z],x]+[[z,x],y] = \sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,[x_{\sigma(1)},x_{\sigma(2)},x_{\sigma(3)}] .
$$

*Proof.* This is *The Symmetric and Antisymmetric Parts of an Algebra Product* §*The Associator Criterion*, proved there by expanding the three terms of the Jacobi sum and collecting the twelve monomials against the six associators; the identity is general and is not redone here. $\square$

**Corollary (the criterion for the block).** For the antisymmetric quaternionic multiplication, half the commutator and half the associator sum stand in the same relation,

$$
J(\tilde P,\tilde Q,\tilde R) = \tfrac14\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)\,[\tilde P_{\sigma(1)},\tilde P_{\sigma(2)},\tilde P_{\sigma(3)}] ,
$$

with the associator taken in the parent quaternionic product. The block is therefore Lie-admissible exactly when the quaternionic product is Lie-admissible, and it is not.

*Proof.* The commutator of the parent product is $[\tilde P,\tilde Q]_{\natural}=2\,\tilde P\diamond\tilde Q$, so the Jacobi sum of the commutator is four times the cyclic sum $J$, and the theorem identifies it with the signed sum of the six associators. The parent product is not associative, so its associator does not vanish, and the criterion is not met. $\square$

The criterion is the exact measure of what associativity would have contributed. It also shows why the block cannot be repaired by a change of sign or of factor: the defect is the associator itself, and it is invisible to the symmetric half, which is central valued.

## The Associator of the Quaternionic Product

**Theorem (the associator).** For the parent product, the associator has the closed form

$$
[\tilde P,\tilde Q,\tilde R] = \bigl(\tilde Q^{\natural}\tilde P-\tilde P^{\natural}\tilde Q^{\natural}\bigr)\tilde R ,
$$

and it is nonzero at $(e_1,e_0,e_0)$ and at $24$ of the $64$ basis triples.

*Proof.* *The Associator and the Ternary Product of the Quaternionic Product* §*The Associator*; the closed form is obtained there by expanding the definition and using that ${}^{\natural}$ is an anti-automorphism of order two. It is not redone here. $\square$

**Computation (the criterion at the witness).** On the triple $(e_0,e_1,e_2)$ the six associators of the parent product are

| ordering | $(\tilde P,\tilde Q,\tilde R)$ | $(\tilde Q,\tilde R,\tilde P)$ | $(\tilde R,\tilde P,\tilde Q)$ | $(\tilde P,\tilde R,\tilde Q)$ | $(\tilde Q,\tilde P,\tilde R)$ | $(\tilde R,\tilde Q,\tilde P)$ |
|---|---|---|---|---|---|---|
| the associator | $0$ | $0$ | $-2e_3$ | $0$ | $2e_3$ | $0$ |

the signed sum of the six is $-4e_3$, and its quarter is the cyclic sum $-e_3$ computed above.

*Proof.* The associator of $(e_0,e_1,e_2)$ is $0$: the parent product reads $e_0^{\natural}e_1 = e_1$ and $e_1^{\natural}e_2 = -e_3$, so $(e_0^{\natural}e_1)^{\natural}e_2 = e_1^{\natural}e_2 = -e_3$ and $e_0^{\natural}(e_1^{\natural}e_2) = e_0^{\natural}(-e_3) = -e_3$, and the two agree. Similarly for the two cyclic images, the surviving ones being $(\tilde R,\tilde P,\tilde Q)=(e_2,e_0,e_1)$ with the associator $-2e_3$ and $(\tilde Q,\tilde P,\tilde R)=(e_1,e_0,e_2)$ with $2e_3$. The six alternate signs in the order of the display, and the two survivors are separated by the ordering that reverses the first two arguments, so the signed sum is $-[2e_3]-[2e_3]=-4e_3$. The quarter is $-e_3$, which is the value of $J(e_0,e_1,e_2)$. $\square$

**Remark.** The two nonzero associators are separated by the transposition of the first two arguments, and the whole failure is the failure of those two to cancel. The identity would hold at this triple if the associator of the parent product vanished on both, and it is the insertion of the conjugation in the first slot of the parent product that prevents it. This is why the block is the one whose defect is non-associativity **alone**: no sesquilinear involution intervenes, and the criterion reads the associator directly.

## The Derived Bracket

**Proposition (the derived bracket is a Lie bracket).** The derived algebra of the block is the vector subspace, $\mathbb{B}\diamond\mathbb{B}=\mathrm{Vect}(\mathbb{B})$, and it is closed under the operation. On it the block is the negative of the cross product, $\tilde P\diamond\tilde Q = -\,\mathbf P\times\mathbf Q$, which satisfies the Jacobi identity; the subalgebra $(\mathrm{Vect}(\mathbb{B}),\diamond)$ is therefore a Lie algebra, isomorphic to $(\mathbb{C}^3,\times)$ and hence to $\mathfrak{sl}(2,\mathbb{C})$.

*Proof.* The image is $\mathrm{Vect}(\mathbb{B})$ and the closure is read on the table, $e_j\diamond e_k=-e_j\times e_k\in\mathrm{Vect}(\mathbb{B})$. On pure vectors the closed form has all three scalar factors zero, so $J$ vanishes identically there and the rest of the Lie axioms are alternation and bilinearity, already established. The cross product on $\mathbb{C}^3$ is the Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ of *The Six Subspaces and the Four General Products*, and the negative is the same bracket with every bracket reversed, which is isomorphic to it. $\square$

**Remark.** The failure of the block is therefore not a failure of its derived bracket but of the extension of that bracket to the whole algebra. The derived bracket is a Lie bracket on the three-dimensional derived subalgebra, and it is exactly the operation $\mathrm{APA}$ of the plain row up to sign; what the block adds to it is the two mixed terms $P_0\mathbf Q-Q_0\mathbf P$ that the scalar part of an element carries into the vector subspace, and it is those terms that break the identity. The block is a Lie bracket on $\mathrm{Vect}(\mathbb{B})$ and not on $\mathbb{B}$.

## The Alternating Centre and the Annihilator

**Proposition.** The alternating centre of the block, the set of $\tilde X$ with $\tilde X\diamond\tilde Y=0$ for all $\tilde Y$, and the annihilator, the set of $\tilde Y$ with $\tilde X\diamond\tilde Y=0$ for all $\tilde X$, are both $\{0\}$. In particular the centre of the algebra $\mathbb{B}$ is not in the centre of the block: a nonzero central element $Ae_0$ satisfies $Ae_0\diamond\tilde Y = A\,\mathbf Y$, which is nonzero as soon as $\tilde Y$ has a nonzero vector part.

*Proof.* Let $\tilde X\diamond\tilde Y=X_0\mathbf Y-Y_0\mathbf X-\mathbf X\times\mathbf Y$ vanish for all $\tilde Y$. At $\tilde Y=e_0$, where $Y_0=1$ and $\mathbf Y=0$, the value is $-\mathbf X$, so $\mathbf X=0$; the element is then $\tilde X=X_0e_0$ and the value at a general $\tilde Y$ is $X_0\mathbf Y$, so $X_0=0$ as well, since the vector subspace is not zero. The same argument with the two slots exchanged gives the annihilator. A central element gives $Ae_0\diamond\tilde Y = A\mathbf Y$, which vanishes for all $\tilde Y$ only when $A=0$. $\square$

The vanishing of the alternating centre is the structural difference between the block and its plain-row counterpart. The bracket of the plain row is the cross product, and there the centre of the algebra is the centre of the bracket, $[\tilde P,\tilde Q]=\mathbf P\times\mathbf Q$ vanishing for every $\tilde Q$ exactly when $\mathbf P=0$. The block of this article is un-centred: its mixed terms make a central element act on every element with a nonzero vector part, and no nonzero element acts trivially on the whole space. The block is thus not a central extension of the cross product but a deformation of it in which the centre has ceased to be central.

## The Elements Whose Adjoint Operators Commute

**Proposition.** Write $L_{\tilde A}$ for the left multiplication operator of the block, $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$. The only element $\tilde B$ with $[L_{\tilde A},L_{\tilde B}]=0$ for all $\tilde A$ is $\tilde B=0$. The centraliser of the four basis operators in the algebra of linear maps is spanned by the identity operator alone, and no nonzero element of $\mathbb{B}$ has its operator in that centraliser.

*Proof.* The identity operator commutes with every operator, so it lies in the centraliser; it is not the operator of an element, since $L_{\tilde B}=c\,\mathrm{id}$ would give $\tilde B\diamond\tilde R=c\,\tilde R$ for all $\tilde R$, and at $\tilde R=e_0$ this is $-\mathbf B=ce_0$, impossible for a pure vector $-\mathbf B$. For the rest, the computation of the operators of the block gives the identity $[L_{\tilde A},L_{\tilde B}]=L_{\tilde A\diamond\tilde B}+D(\tilde A,\tilde B)$ with $D(\tilde A,\tilde B)$ the deviation calculated in *The Adjoint Operators of the Antisymmetric Quaternionic Algebra*; requiring the bracket to vanish for all $\tilde A$ there reduces to a linear system in $\tilde B$, of the sixteen entries of the four basis operators against the four basis elements, whose only solution is $\tilde B=0$. $\square$

**Remark.** The result is the operator echo of the trivial alternating centre. For a Lie algebra the elements whose adjoint operators commute are the elements of the centre of the enveloping algebra; here there are none but the scalars, and the operator-theoretic centre of the block is trivial. The operators article of the block computes the deviation $D$ itself and shows that it is the operator form of the Jacobi failure.

## The Failure on the Basis, the Real Part and the Six Subspaces

**Proposition (the incidence of the failure).** On the basis the cyclic sum is nonzero on $18$ of the $64$ triples, the three unordered triples $\{0,j,k\}$ with their six orderings each. On the real part of the space the same three families are the witnesses, since the basis sits in the real part of the space and the failure needs no genuinely complex coefficient. On the six distinguished subspaces the identity holds on the centre and on the vector subspace and fails on the other four.

*Proof.* The count is the proposition on the basis. On the centre the operation is identically zero, because both arguments have zero vector part, and the identity holds; on the vector subspace no argument has a scalar part, the scalar factors of the closed form vanish, and the identity holds. On the quaternion subspace the triple $(e_0,e_1,e_2)$ lies in the subspace and fails, so the identity fails; on the anti-quaternion subspace the triple $(ie_0,ie_1,ie_2)$ has the imaginary scalar part $i$ and the non-parallel vector parts $ie_1,ie_2$, and the closed form gives $J(ie_0,ie_1,ie_2) = -i\,(ie_1\times ie_2) = i\,e_3$, nonzero; on the Hermitian subspace the triple $(e_0,ie_1,ie_2)$ gives $J = -\,(ie_1\times ie_2) = e_3$, nonzero; on the anti-Hermitian subspace the triple $(ie_0,e_1,e_2)$ gives $J = -i\,(e_1\times e_2) = -ie_3$, nonzero. $\square$

The failure is carried by the two-dimensional piece of every element and not by its class; it survives the restriction to the real part of the space, so it is not a complex phenomenon. This is the same statement as before, read on the subspaces: the defect is the scalar-vector interaction, and every subspace but the centre and the vector subspace carries both a scalar direction and two independent vector directions.

## The Comparison with the Three Jacobi Failures

**Remark.** The catalogue of the twelve records three failures of the Jacobi identity, $\mathrm{AQA}$, $\mathrm{APS}$ and $\mathrm{AQS}$, and assigns three reasons. The block of this article is the one whose reason is non-associativity alone: the parent product is the general quaternionic product, its associator is nonzero, and the associator criterion of *The Symmetric and Antisymmetric Parts of an Algebra Product* reads the failure off that associator with no further obstruction. The two sesquilinear failures have the other reason: for an antisymmetrised sesquilinear product the Jacobi identity needs the collapse of the two involutions, one on each argument, and *Lie Algebras of Sesqualgebras* proves that a genuine sesqualgebra forbids the collapse, so those two blocks fail even when the underlying product is associative. The block of this article has no involution in the class at all — it is $\mathbb{C}$-bilinear — and its defect is the price of the non-associativity of the quaternionic product, not of a sesquilinear slot.

**Remark (the two that hold).** The comparison isolates the two identities that do hold: $\mathrm{APA}$, the cross product, and $\mathrm{SPA}$, the special Jordan product of degree two. The block of this article is separated from $\mathrm{APA}$ by the two mixed terms alone, and it is separated from $\mathrm{SPA}$ by the class and by the alternation. The block is the antisymmetrisation of the quaternionic row where $\mathrm{APA}$ is the antisymmetrisation of the plain row, and the passage from the plain row to the quaternionic row is the insertion of the conjugation in the first slot; that insertion is what costs the Jacobi identity.

## Summary

The cyclic sum of the antisymmetric quaternionic multiplication has the closed form $J(\tilde P,\tilde Q,\tilde R)=-P_0(\mathbf Q\times\mathbf R)+Q_0(\mathbf P\times\mathbf R)-R_0(\mathbf P\times\mathbf Q)$; it is a $\mathbb{C}$-trilinear alternating pure-vector map, and it is decided on the basis, where it is nonzero on the $18$ ordered triples that carry a scalar part and two distinct vector directions, with the minimal witnesses $(e_0,e_1,e_2)$, $(e_0,e_1,e_3)$ and $(e_0,e_2,e_3)$ and values the negatives of the three cross products. The witness of the catalogue is $(e_0,e_1,e_2)$, cyclic sum $-e_3$. The failure is the Lie-admissibility defect of the parent product: by the associator criterion the Jacobi sum of the commutator is the signed sum of the six associators, and here the cyclic sum is a quarter of that signed sum, $J=\tfrac14\sum_\sigma\operatorname{sgn}(\sigma)[\tilde P_{\sigma(1)},\tilde P_{\sigma(2)},\tilde P_{\sigma(3)}]$; on the witness two of the six associators survive, $\pm2e_3$, and their signed sum is $-4e_3$ with the quarter $-e_3$. The defect is non-associativity alone, unlike the two sesquilinear failures, whose cause is the obstruction of *Lie Algebras of Sesqualgebras*. The derived bracket of the block is the negative of the cross product on the derived subalgebra $\mathrm{Vect}(\mathbb{B})$, a Lie algebra isomorphic to $\mathfrak{sl}(2,\mathbb{C})$, and it is a Lie bracket there; the failure is the failure of its extension to the whole algebra, and it needs a scalar part in one argument and non-parallel vector parts in the other two. The alternating centre and the annihilator are both zero, the element whose operator commutes with all the operators is zero, and the identity holds on the centre and on the vector subspace and fails on the other four of the six.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\diamond\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P)$ | the antisymmetric quaternionic multiplication, the operation $\mathrm{AQA}$ |
| $[\tilde P,\tilde Q]_{\natural}=\tilde P^{\natural}\tilde Q-\tilde Q^{\natural}\tilde P$ | the quaternionic bracket, twice the operation |
| $[\tilde P,\tilde Q,\tilde R]=(\tilde P^{\natural}\tilde Q)^{\natural}\tilde R-\tilde P^{\natural}(\tilde Q^{\natural}\tilde R)$ | the associator of the parent product |
| $J(\tilde P,\tilde Q,\tilde R)$ | the cyclic sum $(\tilde P\diamond\tilde Q)\diamond\tilde R+(\tilde Q\diamond\tilde R)\diamond\tilde P+(\tilde R\diamond\tilde P)\diamond\tilde Q$ |
| $J=-P_0(\mathbf Q\times\mathbf R)+Q_0(\mathbf P\times\mathbf R)-R_0(\mathbf P\times\mathbf Q)$ | the closed form of the cyclic sum |
| $J(e_0,e_j,e_k)=-e_j\times e_k$ | the cyclic sum on the basis, nonzero for $j<k$ |
| $J=\tfrac14\sum_\sigma\operatorname{sgn}(\sigma)[\tilde P_{\sigma(1)},\tilde P_{\sigma(2)},\tilde P_{\sigma(3)}]$ | the associator criterion for the block |
| $\mathrm{Vect}(\mathbb{B})$ | the derived subalgebra, on which the block is $-\times$ |
| $L_{\tilde A}\tilde R=\tilde A\diamond\tilde R$ | the left multiplication operator of the block |
| $D(\tilde A,\tilde B)=[L_{\tilde A},L_{\tilde B}]-L_{\tilde A\diamond\tilde B}$ | the operator deviation, the operator form of the failure |

## Further Reading

- *The Symmetric and Antisymmetric Parts of an Algebra Product* (`articles_maths/the-symmetric-and-antisymmetric-parts-of-an-algebra-product.md`), for the associator criterion, the Lie-admissible algebras and the cyclic identity
- *The Associator and the Ternary Product of the Quaternionic Product* (`articles_maths/the-associator-and-the-ternary-product-of-the-quaternionic-product.md`), for the associator of the parent product, its closed form and the count of the basis triples
- *Introduction to the Antisymmetric Quaternionic Algebra of Biquaternions* (`articles_maths/introduction-to-the-antisymmetric-quaternionic-algebra-of-biquaternions.md`), for the operation, its table and its image
- *The Adjoint Operators of the Antisymmetric Quaternionic Algebra* (`articles_maths/the-adjoint-operators-of-the-antisymmetric-quaternionic-algebra.md`), for the deviation $D$ and the derivations of the block
- *Lie Algebras of Sesqualgebras* (`articles_maths/lie-algebras-of-sesqualgebras.md`), for the obstruction that causes the other two Jacobi failures of the twelve
- *The 12 Products of the Biquaternion Complex Space* (`articles_maths/the-12-products-of-the-biquaternion-complex-space.md`), for the three Jacobi rows and their witnesses
- *The Six Subspaces and the Four General Products* (`articles_maths/the-six-subspaces-and-the-four-general-products.md`), for the cross product on the vector subspace and its identification with $\mathfrak{sl}(2,\mathbb{C})$
