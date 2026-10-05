# __The Unitary Operators of a Sesquialgebra__

## Introduction

An element of a sesquialgebra is unitary when its inverse is its conjugate, $uu^{*}=u^{*}u=1$, and the unitary elements form the group that the squaring of the structure singles out. The present article treats the corresponding operators: an operator is **unitary** when its adjoint is its inverse,

$$
T^{\dagger}=T^{-1},
$$

which is the operator analogue of $u^{*}=u^{-1}$ read through the pairing $\varphi(x,y)=\tau(xy^{*})$. The condition is one condition with two parities, since the adjoint of a conjugate-linear operator is taken by the twisted rule: the $R$-linear operators that satisfy it are the unitary operators, the $\varsigma$-semilinear ones are the antiunitary operators, and together they form one group in which the $R$-linear part is a subgroup of index at most two. Restated against the pairing, the condition says that the operator preserves the form, $\varphi(Tx,Ty)=\varphi(x,y)$ for an $R$-linear $T$ and $\varphi(Tx,Ty)=\varsigma\bigl(\varphi(x,y)\bigr)$ for a $\varsigma$-semilinear one; and the operators that preserve the derived product, $T(x\star y)=Tx\star Ty$, are the unital $*$-maps, a class that the article compares with the unitary one.

The subject is the group-theoretic half of the operator theory of the sesquialgebras. The adjoint that the condition is stated with is *The Sesquilinear Adjoint Operator*; the one-sided cases are *The Adjoint of the Conjugate Left Multiplication*, where the operator $L_{u}$ of a unitary element is shown to be antiunitary, and *The Adjoint of the Sesquilinear Sandwich*, where the sandwich with unitary parameters is shown to be unitary; the unitary elements themselves, with their group and their inner $*$-automorphisms, are *Units and the Unitary Elements*; and the involutions that the unitaries induce are *The Involutions of a Sesquialgebra*. In the bilinear layer the same group is *Unitary Operators of an Involutive Algebra* and *Unitary Endomorphisms*; the analysis of the same objects is Part II and Part III, *Bounded Operators on a Sesquialgebra* and the spectral theory of *Unitary Operators*, named as the owners and not used here.

**The boundaries.** The pairing, the two adjoints, the parity obstruction and the scalar laws of the adjoint operation are *The Sesquilinear Adjoint Operator*; the one-sided and two-sided cases are *The Adjoint of the Conjugate Left Multiplication*, *The Adjoint of the Ternary Product* and *The Adjoint of the Sesquilinear Sandwich*; the product-preserving maps are the subject of the last section here and are named beside the *-automorphisms of *Automorphisms and Derivations of Algebras*; and the bilinear analogue of the whole article is *Unitary Operators of an Involutive Algebra*. This article stays inside Part I: no distance, no limit, no completeness.

Throughout, $R$ is a commutative ring with $1$ without zero divisors, $\varsigma$ is an involution of $R$, and $A$ is a unital associative $R$-algebra with a $\varsigma$-semilinear involution $*$, so that $A$ is a sesquialgebra in the sense of *Sesquialgebras*, with $1^{*}=1$. The function $\tau:A\to R$ is $R$-linear, central, $\tau(ab)=\tau(ba)$, and compatible with the involution, $\tau(x^{*})=\varsigma(\tau(x))$, and the pairing $\varphi(x,y)=\tau(xy^{*})$ is $R$-linear in the first variable, $\varsigma$-semilinear in the second and perfect. The derived product is $x\star y=xy^{*}$, the operators are $L_{a}(x)=ax^{*}$, $R_{b}(x)=xb^{*}$, $S_{a,b}(x)=ax^{*}b$ and $T_{p,q}(x)=pxq$, the unitary elements are $U(A)=\{u:uu^{*}=u^{*}u=1\}$, and $\alpha_{u}(x)=uxu^{*}$ is the inner $*$-automorphism of a unitary element $u$. The adjoint of a $\varsigma$-semilinear $S$ is defined by $\varphi(Sx,y)=\varsigma\bigl(\varphi(x,S^{\dagger}y)\bigr)$ and that of an $R$-linear $T$ by $\varphi(Tx,y)=\varphi(x,T^{\dagger}y)$, both existing and unique by *The Sesquilinear Adjoint Operator*.

## The Unitary Condition

### The Definition and its Readings

**Definition.** An operator $T:A\to A$ of one of the two parities, so that its adjoint is defined, is **unitary** when it is invertible and

$$
T^{\dagger}T=TT^{\dagger}=\mathrm{id},
$$

equivalently when $T^{\dagger}=T^{-1}$; an $R$-linear one is a **unitary operator**, and a $\varsigma$-semilinear one is an **antiunitary operator**.

**Theorem (the readings of the condition).** For an invertible operator $T$ of one of the two parities the following are equivalent:

(i) $T^{\dagger}=T^{-1}$, that is $T^{\dagger}T=TT^{\dagger}=\mathrm{id}$;

(ii) $T^{\dagger}T=\mathrm{id}$;

(iii) $\varphi(Tx,Ty)=\varphi(x,y)$ for all $x,y$, when $T$ is $R$-linear;

(iv) $\varphi(Tx,Ty)=\varsigma\bigl(\varphi(x,y)\bigr)$ for all $x,y$, when $T$ is $\varsigma$-semilinear.

**Proof.** (i) $\Leftrightarrow$ (ii) holds because $T^{\dagger}T=\mathrm{id}$ makes $T$ injective and $T$ is invertible by hypothesis, so $T^{\dagger}$ is the two-sided inverse. For (ii) $\Leftrightarrow$ (iii), the linear rule gives $\varphi(Tx,Ty)=\varphi(x,T^{\dagger}Ty)$, so the condition holds for all $x,y$ exactly when $\varphi(x,T^{\dagger}Ty)=\varphi(x,y)$ for all $x,y$, which by the perfection of $\varphi$ is $T^{\dagger}T=\mathrm{id}$. For (iv), the twisted rule gives $\varphi(Tx,Ty)=\varsigma\bigl(\varphi(x,T^{\dagger}Ty)\bigr)$, and the condition therefore reads $\varsigma\bigl(\varphi(x,T^{\dagger}Ty)\bigr)=\varsigma\bigl(\varphi(x,y)\bigr)$, which is $T^{\dagger}T=\mathrm{id}$ again. $\square$

**Remark (the form is preserved up to the twist).** A unitary operator is an isometry of $\varphi$ and an antiunitary operator is an isometry up to the base involution; in the bilinear case $\varsigma=\mathrm{id}$ the two readings coincide and both are $\varphi(Tx,Ty)=\varphi(x,y)$. The reading (iii) is the operator form of the unitary element of a form, and (iv) is the operator form of the antiunitary one.

### The Two Parities

**Theorem (the group).** The invertible operators with $T^{\dagger}T=\mathrm{id}$ form a group $G$; the $R$-linear ones form a subgroup $G_{0}$, the **unitary group**, which is of index at most two and invariant under conjugation in $G$, and the $\varsigma$-semilinear ones, the **antiunitary operators**, form the complementary coset when it is nonempty. The adjoint operation $T\mapsto T^{\dagger}$ is an anti-automorphism of order two of $G$, it carries $G_{0}$ to itself and the coset to itself, and inversion does the same.

**Proof.** The composite of two operators with $T^{\dagger}T=\mathrm{id}$ has $(ST)^{\dagger}(ST)=T^{\dagger}S^{\dagger}ST=T^{\dagger}T=\mathrm{id}$ by the anti-multiplicativity of the adjoint, and the identity is unitary, so $G$ is a group; the inverse of a unitary operator is its adjoint, which satisfies the condition by the law of order two. The parity is multiplicative for the composite, a product of two operators of the same parity being $R$-linear and of two of opposite parity being $\varsigma$-semilinear, so the $R$-linear elements are the kernel of a homomorphism of $G$ onto a subgroup of the two-element group, whence a subgroup of index at most two that is invariant under conjugation; the $\varsigma$-semilinear elements are the other coset. The adjoint law $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$, the law $(T^{\dagger})^{\dagger}=T$ and the scalar laws of *The Sesquilinear Adjoint Operator* give the remaining statements, and inversion is a word in the adjoint on $G$. $\square$

**Remark (the two adjoints).** Every element of $G$ is an isometry of the pairing, and since the pairing of a sesquialgebra is sesqui-symmetric the adjoint and the left adjoint coincide, ${}^{\dagger}S=S^{\dagger}$, by the theorem of *The Sesquilinear Adjoint Operator*; so there is no second unitary group attached to the transposed pairing, and the antiunitary operators are not a second group but the second coset of one group. This is the point at which the sesqui-symmetric pairing removes the defect of a general one, where the two adjoints differ and a conjugate-linear operator carries two of them.

## The Relation to the Unitary Elements

**Theorem (the one-sided operators).** Let $u\in U(A)$. Then

$$
L_{u}^{\dagger}=S_{1,u}=L_{u}^{-1},
$$

so the conjugate left multiplication by a unitary element is an antiunitary operator; and $R_{b}$ is a unitary operator exactly when $b$ is a unitary element, $R_{b}^{\dagger}=R_{b^{*}}$, $R_{b}^{-1}=R_{b^{-1}}$.

**Proof.** For the left multiplication, $L_{u}=S_{u,1}$ and the adjoint of the sandwich is $S_{1,u}$; and $L_{u}(S_{1,u}x)=u(x^{*}u)^{*}=uu^{*}x=x$, $S_{1,u}(L_{u}x)=(ux^{*})^{*}u=xu^{*}u=x$, so the inverse is $S_{1,u}$, the two identities holding because $u$ is unitary. For the right multiplication, $R_{b}$ is $R$-linear with $R_{b}^{\dagger}=R_{b^{*}}$, and $R_{b}(R_{b^{-1}}x)=xb^{-1}b=x$ and $R_{b^{-1}}(R_{b}x)=xbb^{-1}=x$, so $R_{b}^{-1}=R_{b^{-1}}$; the adjoint and the inverse agree exactly when $b^{*}=b^{-1}$, that is when $b$ is unitary. $\square$

**Theorem (the inner $*$-automorphisms).** Let $u\in U(A)$. Then $\alpha_{u}(x)=uxu^{*}$ is an $R$-linear unitary operator, with

$$
\alpha_{u}^{\dagger}=\alpha_{u^{*}}=\alpha_{u}^{-1}.
$$

**Proof.** The linearity and the multiplicativity are those of the inner $*$-automorphism; for the adjoint, $\varphi(\alpha_{u}x,y)=\tau(uxu^{*}y^{*})=\tau(xu^{*}y^{*}u)=\varphi(x,\alpha_{u^{*}}y)$ by the centrality of $\tau$, so $\alpha_{u}^{\dagger}=\alpha_{u^{*}}$; and $\alpha_{u^{*}}=\alpha_{u^{-1}}=\alpha_{u}^{-1}$ because $u$ is unitary. $\square$

**Corollary (the maps from the group of the elements).** For a unitary $u$ the sandwich $S_{a,b}$ with $a=u$, $b=1$ is antiunitary and with $a,b\in U(A)$ is unitary; and the assignments $u\mapsto L_{u}$, $u\mapsto R_{u}$ and $u\mapsto\alpha_{u}$ carry $U(A)$ into $G$, the first into the antiunitary coset and the last two into $G_{0}$. The kernel of $u\mapsto\alpha_{u}$ is the group $U(A)\cap Z(A)$ of the central unitary elements, and $u\mapsto L_{u}$ and $u\mapsto R_{u}$ are injective.

**Proof.** The antiunitarity of $L_{u}$ and the unitarity of $S_{u,v}$ are the theorems above and the corollary of *The Adjoint of the Sesquilinear Sandwich*; the unitarity of $R_{u}$ and $\alpha_{u}$ are the theorems above. The kernel of $u\mapsto\alpha_{u}$ is the set of unitary $u$ with $uxu^{*}=x$, that is $ux=xu$ for all $x$, which is $U(A)\cap Z(A)$; and $L_{u}=L_{u'}$ forces $u=L_{u}(1)=L_{u'}(1)=u'$, so $u\mapsto L_{u}$ is injective, and $R_{b}=R_{b'}$ forces $b^{*}=b'^{*}$ at $x=1$. $\square$

**Remark (the picture).** The group of the elements therefore sits inside the unitary group of the operators in three ways: the right multiplications and the inner automorphisms give the $R$-linear part, and the left multiplications give the $\varsigma$-semilinear part. As maps of sets the three are injective, but they are not all multiplicative: $u\mapsto\alpha_{u}$ and $u\mapsto R_{u}$ are homomorphisms, $R_{u}R_{v}=R_{uv}$, while $u\mapsto L_{u}$ is not, its composite $L_{u}L_{v}=T_{u,\,v^{*}}$ leaving the one-sided family. The antilinear character of the left regular representation, which *The Left and Right Multiplication Operators of a Sesquialgebra* records as the reason no single linear representation carries the whole product, appears here as the reason half of the image of $U(A)$ is antiunitary.

## The Operators that Preserve the Product

**Theorem.** Let $T$ be an $R$-linear operator with $T(1)=1$. Then $T$ preserves the derived product,

$$
T(x\star y)=Tx\star Ty\qquad\text{for all }x,y,
$$

if and only if $T$ is a unital $*$-map: $T(xy)=Tx\,Ty$ and $T(y^{*})=(Ty)^{*}$ for all $x,y$.

**Proof.** If $T$ is a unital $*$-map then $T(xy^{*})=Tx\,T(y^{*})=Tx\,(Ty)^{*}=Tx\star Ty$. Conversely, put $y=1$ and then replace $y$ by $y^{*}$: the identity is $T(xy^{*})=Tx(Ty)^{*}$, so $T(x)=Tx\,(T1)^{*}=Tx$ at $y=1$, and $T(y^{*})=T(1\cdot y^{*})=T1\,(Ty)^{*}=(Ty)^{*}$ at $x=1$, which is the second law; then $T(xy)=T(x(y^{*})^{*})=Tx\,(T(y^{*}))^{*}=Tx\,Ty$, which is the first. $\square$

**Proposition.** An invertible unital $*$-map that preserves the product is unitary exactly when it also preserves $\tau$, $\tau\circ T=\tau$; and every inner $*$-automorphism $\alpha_{u}$ of a unitary $u$ preserves $\tau$ and is therefore unitary.

**Proof.** For such a $T$, $\varphi(Tx,Ty)=\tau(Tx\,(Ty)^{*})=\tau\bigl(T(xy^{*})\bigr)=(\tau\circ T)(xy^{*})$, which equals $\varphi(x,y)=\tau(xy^{*})$ for all $x,y$ exactly when $\tau\circ T=\tau$, by the perfection of $\varphi$. For the inner map, $\tau\alpha_{u}(x)=\tau(uxu^{*})=\tau(xu^{*}u)=\tau(x)$ by the centrality of $\tau$ and $u^{*}u=1$. $\square$

**Remark (the two classes are different).** The product-preserving condition and the unitary condition are not the same. The conjugate left multiplication $L_{u}$ of a unitary element is antiunitary, $L_{u}^{\dagger}=L_{u}^{-1}$, and it does not preserve the product, since

$$
L_{u}(x\star y)=u\,y\,x^{*}\quad\text{against}\quad L_{u}x\star L_{u}y=u\,x^{*}\,y\,u^{*},
$$

which differ unless $x$ and $y$ commute suitably; in particular $L_{1}$ is the involution, an anti-automorphism that reverses the product. So the two conditions are independent: a unitary operator need not preserve the product, and a product-preserving map is unitary exactly when it also preserves $\tau$, as the proposition above states.

## Worked Case: the Complex Matrices

Let $A=M_{n}(\mathbb{C})$ with the conjugate transpose, $\varsigma$ the complex conjugation, $\tau=\operatorname{tr}$ and $\varphi(X,Y)=\operatorname{tr}(XY^{*})$. The unitary elements are the unitary matrices, and the general theory fixes the two-sided families of the unitary and the antiunitary operators as follows.

**Proposition (the two-sided family).** For unitary matrices $U,V$ the operator $T_{U,V}(X)=UXV$ is unitary, the composite is $T_{U,V}T_{U',V'}=T_{UU',V'V}$, and the parametrisation has the central unitary elements as its kernel, $T_{cU,c^{-1}V}=T_{U,V}$ for a scalar $c$ of unit modulus. The operator $T_{U,V}$ is multiplicative exactly when $V=U^{*}$, in which case it is the inner $*$-automorphism $\alpha_{U}$; so the multiplicative unitary operators of $M_{n}(\mathbb{C})$ are exactly the inner $*$-automorphisms, and their own parametrisation has the central unitary matrices as kernel.

**Proof.** The unitarity is $\varphi(UXV,UYV)=\operatorname{tr}\bigl(UXV\,V^{*}Y^{*}U^{*}\bigr)=\operatorname{tr}(XY^{*})$ for unitary $U,V$, and the composite is $U(U'XV')V=UU'X\,V'V$. The kernel is read as in the kernel proposition of *The Sesquilinear Sandwich Operator*: $T_{cU,c^{-1}V}=T_{U,V}$ for a central $c$, and conversely $T_{U,V}=T_{U',V'}$ forces $U'=cU$ and $V'=c^{-1}V$ for a central unitary $c$. For the multiplicativity, $T_{U,V}(XY)=U\,XY\,V$ while $T_{U,V}(X)T_{U,V}(Y)=U\,X\,VU\,Y\,V$, and the two agree for all $X,Y$ exactly when $VU=1$, that is when $V=U^{*}$; then $T_{U,U^{*}}=\alpha_{U}$. The identification of the multiplicative unitary operators is the proposition above, that a product-preserving invertible operator is unitary exactly when it preserves $\tau$, together with the theorem of *Inner Automorphisms of a Ring* that every automorphism of $M_{n}(\mathbb{C})$ is inner. $\square$

**Proposition (the antiunitary family).** For unitary matrices $U,V$ the operator $X\mapsto U\overline{X}V$ is antiunitary; it is multiplicative exactly when $V=U^{*}$, and then it is the composite $\alpha_{U}\circ\overline{(\cdot)}$ of an inner $*$-automorphism with the conjugation of the matrices.

**Proof.** The conjugation $X\mapsto\overline{X}$ is $\varsigma$-semilinear and an antiunitary isometry, $\varphi\bigl(\overline{X},\overline{Y}\bigr)=\operatorname{tr}\bigl(\overline{X}\,Y^{T}\bigr)=\sum_{i,j}\overline{X_{ij}}\,Y_{ij}=\varsigma\bigl(\operatorname{tr}(X\overline{Y})\bigr)=\varsigma\bigl(\varphi(X,Y)\bigr)$; the $R$-linear $T_{U,V}$ is unitary, and a composite of an antiunitary operator with a unitary one is antiunitary, which is the first clause. The multiplicativity is the computation of the proposition above, the conjugation being multiplicative, $\overline{XY}=\overline{X}\,\overline{Y}$, and the case $V=U^{*}$ is the composite $\alpha_{U}\circ\overline{(\cdot)}$. $\square$

**Remark.** The unitary operators are strictly larger than the $*$-automorphisms, and the families displayed do not exhaust them either: the transpose $X\mapsto X^{T}$ is an $R$-linear unitary operator that is not of the form $X\mapsto UXV$. The example therefore illustrates, without classifying the whole group, the separation of the two classes of the preceding section. With $\mathbb{H}$ in place of $\mathbb{C}$ the base involution is the identity, every operator is $R$-linear, and the antiunitary coset is empty; the group is the $R$-linear one, the degeneration that *Unitary Operators of an Involutive Algebra* develops in the bilinear layer with $\varsigma=\mathrm{id}$.

## Summary

An operator of a sesquialgebra is unitary when its adjoint is its inverse, $T^{\dagger}=T^{-1}$, equivalently $T^{\dagger}T=\mathrm{id}$; against the pairing this is the isometry condition $\varphi(Tx,Ty)=\varphi(x,y)$ for an $R$-linear operator and the twisted isometry $\varphi(Tx,Ty)=\varsigma(\varphi(x,y))$ for a $\varsigma$-semilinear one. The condition has two parities, and the operators that satisfy it form a group $G$ in which the $R$-linear ones, the unitary operators, are a subgroup $G_{0}$ of index at most two, invariant under conjugation in $G$, the $\varsigma$-semilinear ones being the antiunitary coset; the adjoint is an anti-automorphism of order two of $G$ carrying each coset to itself.

The unitary elements inject into $G$ through their one-sided operators: the conjugate left multiplication of a unitary element is antiunitary, $L_{u}^{\dagger}=S_{1,u}=L_{u}^{-1}$, the right multiplication is unitary exactly for a unitary element, $R_{b}^{\dagger}=R_{b^{*}}$ with $R_{b}^{-1}=R_{b^{-1}}$, and the inner $*$-automorphism is unitary, $\alpha_{u}^{\dagger}=\alpha_{u^{*}}=\alpha_{u}^{-1}$, with kernel the central unitary elements. The operators that preserve the product, $T(x\star y)=Tx\star Ty$, are the unital $*$-maps, and they are unitary exactly when they also preserve $\tau$; the two conditions are independent, the left multiplication being antiunitary and not preserving the product. In $M_{n}(\mathbb{C})$ the operators $X\mapsto UXV$ with $U,V$ unitary are unitary and those with $V=U^{*}$ are the inner $*$-automorphisms $X\mapsto UXU^{*}$, while the operators $X\mapsto U\overline{X}V$ are antiunitary; the unitary operators are strictly more than the $*$-automorphisms, the transpose $X\mapsto X^{T}$ being an example.

## Summary of Notation

| symbol | meaning |
|---|---|
| $T^{\dagger}=T^{-1}$ | the unitary condition, the adjoint is the inverse |
| $T^{\dagger}T=TT^{\dagger}=\mathrm{id}$ | the same condition in the two-sided form |
| $\varphi(Tx,Ty)=\varphi(x,y)$ | the isometry reading, $R$-linear $T$ |
| $\varphi(Tx,Ty)=\varsigma(\varphi(x,y))$ | the twisted isometry reading, $\varsigma$-semilinear $T$ |
| unitary / antiunitary | $R$-linear / $\varsigma$-semilinear operator with $T^{\dagger}=T^{-1}$ |
| $G$, $G_{0}$ | the unitary group of the operators and its $R$-linear subgroup |
| $L_{u}^{\dagger}=S_{1,u}=L_{u}^{-1}$ | the left multiplication of a unitary element is antiunitary |
| $R_{b}^{\dagger}=R_{b^{*}}$, $R_{b}^{-1}=R_{b^{-1}}$ | the right multiplication is unitary exactly for $b$ unitary |
| $\alpha_{u}^{\dagger}=\alpha_{u^{*}}=\alpha_{u}^{-1}$ | the inner $*$-automorphism is unitary |
| $T(x\star y)=Tx\star Ty$ | the product-preserving condition |
| $U(A)\cap Z(A)$ | the kernel of the inner $*$-automorphism map |
| $X\mapsto UXV$, $X\mapsto U\overline{X}V$ | the unitary and the antiunitary operators of $M_{n}(\mathbb{C})$ |

## Further Reading

- Sterling K. Berberian, *Baer $\ast$-Rings* (Springer, 1972), for the adjoint operation in a ring with an involution, the module of the conjugate-linear operators and the unitary and antiunitary operators built from the two rules.
- Irving Kaplansky, *Rings of Operators* (W. A. Benjamin, 1968), for the unitary group of an operator algebra and its relation to the $*$-automorphisms and the inner automorphisms.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the unitary elements, the inner $*$-automorphisms they induce and the operators attached to a ring with an involution.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the unitary and antiunitary operators and their use, treated there with the analysis the present article leaves to Part III.
- The companion articles of this series: *The Sesquilinear Adjoint Operator*, *The Adjoint of the Conjugate Left Multiplication*, *The Adjoint of the Sesquilinear Sandwich*, *The Adjoint of the Ternary Product*, *The Left and Right Multiplication Operators of a Sesquialgebra*, *Units and the Unitary Elements*, *The Involutions of a Sesquialgebra* and *Unitary Operators of an Involutive Algebra*.
