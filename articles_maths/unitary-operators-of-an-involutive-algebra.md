# __Unitary Operators of an Involutive Algebra__

## Introduction

An involution of the operator algebra distinguishes among the operators those that it carries to their inverse: an operator $T$ is **unitary** for the involution when $T^{*}T=TT^{*}=\mathrm{id}$, and the unitary operators form a group — the fixed subgroup of the automorphism $\theta(T)=(T^{*})^{-1}$ of the unit group, and the operator analogue of the group of unitary elements of an involutive algebra. The two groups are related by the regular representation: the assignment $a \mapsto L_a$ carries a unitary element of $A$ to a unitary operator of $E$, and against the twisted pairing this assignment is a `*`-representation, so that the unitary group of the algebra appears as a subgroup of the unitary group of its operators. The operator group is in general larger, and its Lie algebra is the space of the skew-adjoint operators.

This article develops the unitary operators of an involutive algebra, the group they form, the self-adjoint and the skew-adjoint operators beside them, the two unitary groups attached to the two pairings of the category, and the map from the unitary elements of the algebra into the unitary operators. It assumes the operator algebra and its involution of *Involutions of the Operator Algebra*, the adjoint operation and the twisted pairing of *The Adjoint in an Involutive Algebra*, the trace and the pairing of *Frobenius Algebras*, the involutions of an algebra of *Involutive Linear Algebras*, the unitary elements, the self-adjoint part and the Lie algebra of the skew elements of *Unitary Elements of an Involutive Algebra* and *The Self-Adjoint Part of an Algebra*, and the one-sided multiplications of *Left and Right Multiplication*. The adjoints of the one-sided and the signed operators are *The Adjoint of the Left Multiplication on an Algebra* and *The Signed Adjoint Sandwich on an Algebra*; the analytic unitary group, the norm and the positivity are Part II and *Hilbert Algebras* and *Operator Algebras*, named as the owner and not used.

Throughout, $k$ is a field of characteristic not two, $A$ is a finite-dimensional unital associative $k$-algebra, $\tau$ is a trace with a nondegenerate pairing $\langle x,y\rangle=\tau(xy)$, $\sigma$ is an involution of $A$ with $\tau(\sigma(x))=\tau(x)$, and $E=\operatorname{End}_k(A)$ is the operator algebra with the involution $T\mapsto T^{*}$ for the plain pairing and $T\mapsto T^{*_\sigma}$ for the twisted pairing $\{x,y\}=\tau(x\sigma(y))$. The unitary groups are written $U(E)=U(E,*)$ and $U(E,*_\sigma)$ for the two pairings, and $U(A)=U(A,\sigma)$ for the group of unitary elements of the algebra.

## The Two Unitary Groups of the Operators

**Definition.** An operator $T \in E$ is **unitary** for the plain pairing when

$$
T^{*}T=TT^{*}=\mathrm{id},
$$

and **unitary for the twisted pairing** when the same equations hold with $T^{*_\sigma}$ in place of $T^{*}$. The sets of such operators are written $U(E)=U(E,*)$ and $U(E,*_\sigma)$.

**Theorem.** $U(E)$ and $U(E,*_\sigma)$ are subgroups of the unit group $E^{\times}$, and

$$
T \in U(E) \iff T \in E^{\times} \text{ and } T^{*}=T^{-1}, \qquad T \in U(E,*_\sigma) \iff T \in E^{\times} \text{ and } T^{*_\sigma}=T^{-1} .
$$

Each is the fixed subgroup of the order-two automorphism $\theta(T)=(T^{*})^{-1}$, respectively $\theta_\sigma(T)=(T^{*_\sigma})^{-1}$, of $E^{\times}$, and each contains the identity and is closed under the adjoint and under inversion.

*Proof.* The equivalence is the definition read as the two halves of invertibility: the two equations say that $T^{*}$ is the two-sided inverse of $T$. That the fixed subgroup of an order-two automorphism of a group is a subgroup, that the identity is fixed, and that the fixed set is closed under inversion and under the automorphism are the general theory of *Unitary Elements of an Involutive Algebra*, applied to the involutive algebra $(E,*)$ and to $(E,*_\sigma)$; the involution maps a unitary operator to its inverse because $T^{*_\sigma}T=\mathrm{id}$ is equivalent to $T^{*_\sigma}=T^{-1}$.

**Corollary (the involution on the operators extends the involution of the algebra).** The unitary operators are exactly the operators that the automorphism $\theta(T)=(T^{*})^{-1}$ fixes, and the maps $T\mapsto T^{*}$ and $T\mapsto T^{-1}$ agree on $U(E)$; in particular $U(E)$ is stable under the involution and $\theta$ restricts to the identity on it.

*Proof.* The first statement is the theorem; on a unitary operator $T^{*}=T^{-1}$, so the involution and the inversion coincide there, and $\theta(T)=(T^{*})^{-1}=(T^{-1})^{-1}=T$.

## The Self-Adjoint and Skew-Adjoint Operators

**Definition.** The **self-adjoint operators** $E^{+}$ and the **skew-adjoint operators** $E^{-}$ are those with $T^{*}=T$ and with $T^{*}=-T$; for the twisted involution they are written $E^{+}_\sigma$ and $E^{-}_\sigma$.

**Theorem.** For every unitary operator $u \in U(E)$ the operators $u+u^{*}$ and $u u^{*}$ are self-adjoint and $u-u^{*}$ is skew-adjoint, and

$$
u=\tfrac12\bigl(u+u^{*}\bigr)+\tfrac12\bigl(u-u^{*}\bigr), \qquad (u+u^{*})^{*}=u+u^{*}, \qquad (u-u^{*})^{*}=-(u-u^{*}), \qquad (uu^{*})^{*}=uu^{*}=1 .
$$

*Proof.* Apply $*$ and use $(ST)^{*}=S^{*}T^{*}$ and $u^{*}=u^{-1}$: $(u+u^{*})^{*}=u^{*}+u=u+u^{*}$, $(u-u^{*})^{*}=u^{*}-u=-(u-u^{*})$, and $(uu^{*})^{*}=u^{**}u^{*}=uu^{*}$, which is $1$ for a unitary $u$. This is the computation of *Unitary Elements of an Involutive Algebra* carried out in the involutive algebra $(E,*)$.

**Corollary (the Lie algebra of the unitary group).** The skew-adjoint operators $E^{-}$ are the algebraic tangent space of $U(E)$ at the identity, and with the commutator they form a Lie algebra; the self-adjoint operators $E^{+}$ with the symmetrised product form a Jordan algebra, and the two are the Jordan–Lie pair of the involution of *Involutions of the Operator Algebra*.

*Proof.* The statements are *The Self-Adjoint Part of an Algebra* and *Unitary Elements of an Involutive Algebra* applied to $(E,*)$; for skew-adjoint $T$ and $S$ one has $[T,S]^{*}=[S^{*},T^{*}]=[-S,-T]=[S,T]=-[T,S]$, so a commutator of skew-adjoint operators is skew-adjoint.

## The Two Pairings and the Unitary Groups

**Theorem.** The conjugation $c_{\sigma}(T)=\sigma T\sigma$ is an involutive automorphism of $E$ that carries the plain unitary group isomorphically onto the twisted one,

$$
c_{\sigma}\bigl(U(E)\bigr)=U(E,*_\sigma), \qquad c_{\sigma}\bigl(U(E,*_\sigma)\bigr)=U(E),
$$

and it carries $E^{+}$ onto $E^{+}_\sigma$ and $E^{-}$ onto $E^{-}_\sigma$.

*Proof.* The dictionary $T^{*_\sigma}=\sigma T^{*}\sigma$ of *The Adjoint in an Involutive Algebra* gives $c_{\sigma}(T^{*})=T^{*_\sigma}$, and $c_{\sigma}$ is multiplicative; hence $c_{\sigma}(T^{*}T)=c_{\sigma}(T^{*})c_{\sigma}(T)=T^{*_\sigma}c_{\sigma}(T)$, and $T^{*}T=\mathrm{id}$ is carried to $T^{*_\sigma}c_{\sigma}(T)=\mathrm{id}$, which is the unitarity of $c_{\sigma}(T)$ for the twisted pairing. The reverse implication is the same with $\sigma$ exchanged, and the fixed parts are carried because $c_{\sigma}$ commutes with the two involutions up to the dictionary.

**Corollary.** If the adjoint of $T$ commutes with $\sigma$ then $T$ is unitary for the plain pairing exactly when it is unitary for the twisted one, and then $c_{\sigma}(T)=T$.

*Proof.* On such a $T$ the two adjoints coincide by the corollary of *The Adjoint in an Involutive Algebra*, so the two unitarity conditions are the same equation.

## The Unitary Elements of the Algebra

**Theorem.** The left regular representation $L : A \to E$, $a \mapsto L_a$, is an injective $k$-algebra homomorphism satisfying

$$
L_{\sigma(a)}=L_a^{*_\sigma} ;
$$

hence it restricts to an injective homomorphism of groups

$$
L : U(A,\sigma) \longrightarrow U(E,*_\sigma), \qquad u \longmapsto L_u,
$$

so the unitary elements of the algebra form a subgroup of the unitary operators, isomorphic to $U(A,\sigma)$.

*Proof.* Injectivity is $L_a=0 \Rightarrow a=L_a 1=0$. The intertwining identity is the corollary of *The Adjoint in an Involutive Algebra*, $L(\sigma(a))=L(a)^{*_\sigma}$. For $u \in U(A)$ one has $\sigma(u)u=1$ and $u\sigma(u)=1$, so $L_u^{*_\sigma}L_u=L_{\sigma(u)}L_u=L_{\sigma(u)u}=L_1=\mathrm{id}$ and similarly in the other order; hence $L_u$ is unitary for the twisted pairing. The restriction is injective because $L$ is, and it is a homomorphism because $L$ is multiplicative.

**Corollary.** The right regular representation $R : a \mapsto R_a$ is an injective anti-homomorphism carrying $U(A,\sigma)$ into $U(E,*_\sigma)$ as well, since $R_{\sigma(a)}=R_a^{*_\sigma}$; the two images are exchanged by the adjoint, and together they generate the two-sided representation of the algebra by unitary operators.

*Proof.* $R$ reverses products, $R_{ab}=R_bR_a$, and the identity $R_{\sigma(a)}=R_a^{*_\sigma}$ is the right-hand case of the adjoint theorem; the arguments of the preceding theorem then apply with the order reversed.

**Corollary.** The subgroup generated by the left and the right regular images of $U(A,\sigma)$ is a subgroup of $U(E,*_\sigma)$, and the two-sided operators $T_{a,b}$ with $a$ and $b$ unitary are unitary operators of the twisted pairing.

*Proof.* A product of unitary operators is unitary, and $T_{a,b}=L_aR_b$ is a product of two unitary operators, hence unitary; the general two-sided statement is *The Signed Adjoint Sandwich on an Algebra*.

## Examples

**(a) The matrix algebra with the transpose.** For $A=M_n(k)$ with $\sigma$ the transpose and $\tau=\operatorname{Tr}$, a matrix $X$ is unitary in the algebra exactly when $X^{\mathsf{T}}X=1$, that is when $X$ is orthogonal over $k$; the left and the right multiplications by such an $X$ are unitary operators for the coefficient pairing $\{X,Y\}=\sum X_{ij}Y_{ij}$. Over $\mathbb{R}$ the group is the orthogonal group of order $n$, and over $\mathbb{C}$ with the conjugate transpose it is the unitary group, which is Part II.

**(b) The group algebra.** For $A=k[G]$ with $\sigma(g)=g^{-1}$, every group element is unitary, $U(A)=G$, and the left regular representation $g \mapsto L_g$ is an injective homomorphism of $G$ into the unitary operators for the pairing $\{g,h\}=\delta_{g,h}$; the right regular representation gives the other copy, and the two-sided operators $T_{g,h}$ with $g,h \in G$ are unitary operators for this pairing as well.

**(c) The trivial involution.** For $\sigma=\mathrm{id}$ the twisted pairing is the plain one, the two unitary groups coincide, and the unitary elements are the elements with $u^{2}=1$; the unitary operators are the operators with $T^{*}=T^{-1}$ for the plain pairing.

**(d) The identity and the scalars.** The identity operator is unitary in every case, and a scalar operator $\lambda\,\mathrm{id}$ is unitary exactly when $\lambda^{2}=1$; the scalars therefore contribute the two-element group $\{\pm\mathrm{id}\}$ in characteristic not two, and this is the kernel of the map from the unitary operators to the projective ones, whose study belongs to the representations of the algebra.

## Summary

An operator $T \in E=\operatorname{End}_k(A)$ is **unitary** for the involution $*$ when $T^{*}T=TT^{*}=\mathrm{id}$, equivalently when it is invertible with $T^{*}=T^{-1}$, and the unitary operators form a subgroup $U(E)$ of $E^{\times}$ — the fixed subgroup of the order-two automorphism $\theta(T)=(T^{*})^{-1}$. Beside it sit the self-adjoint operators $E^{+}$, with the symmetrised product a Jordan algebra, and the skew-adjoint operators $E^{-}$, with the commutator a Lie algebra and the tangent space of $U(E)$ at the identity; the unitary $u$ decomposes as $u=\tfrac12(u+u^{*})+\tfrac12(u-u^{*})$ into a self-adjoint and a skew-adjoint part. The twisted pairing gives a second unitary group $U(E,*_\sigma)$, and the conjugation $c_{\sigma}(T)=\sigma T\sigma$ is an isomorphism $U(E)\to U(E,*_\sigma)$ carrying the fixed parts accordingly. The left regular representation is an injective $*$-homomorphism $(A,\sigma)\to(E,*_\sigma)$, so it carries the unitary elements $U(A,\sigma)$ isomorphically onto a subgroup of the unitary operators, and the right representation gives the other copy; the two-sided unitary operators of the twisted pairing include all products $T_{a,b}=L_aR_b$ with $a,b$ unitary. The operator unitary group is in general larger than the image of the elements, and its analytic reading — the norm, the positivity, the Hilbert-space unitary group — is Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=\operatorname{End}_k(A)$ | the operator algebra |
| $T^{*}$, $T^{*_\sigma}$ | the adjoints for the plain and the twisted pairings |
| $U(E)=U(E,*)$ | the unitary operators, $T^{*}T=TT^{*}=\mathrm{id}$ |
| $U(E,*_\sigma)$ | the unitary operators for the twisted pairing |
| $\theta(T)=(T^{*})^{-1}$ | the order-two automorphism whose fixed subgroup is $U(E)$ |
| $E^{+}$, $E^{-}$ | the self-adjoint and the skew-adjoint operators |
| $E^{+}_\sigma$, $E^{-}_\sigma$ | the same for the twisted involution |
| $c_{\sigma}(T)=\sigma T\sigma$ | the conjugation, an isomorphism $U(E)\to U(E,*_\sigma)$ |
| $L$, $R$ | the left and the right regular representations |
| $L_{\sigma(a)}=L(a)^{*_\sigma}$, $R_{\sigma(a)}=R(a)^{*_\sigma}$ | the regular representations as `*`-representations |
| $U(A)=U(A,\sigma)$ | the unitary elements of the algebra, mapped into $U(E,*_\sigma)$ |
| $u=\tfrac12(u+u^{*})+\tfrac12(u-u^{*})$ | the self-adjoint and skew-adjoint decomposition of a unitary |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the unitary elements, the self-adjoint part and the decomposition of a unitary element.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the unitary group of an algebra with involution and the operators of the regular representation.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the unitary group of an algebra with involution and its Lie algebra.
- K. R. Goodearl and R. B. Warfield, *An Introduction to Noncommutative Noetherian Rings* (Cambridge University Press, 1989), for the endomorphism algebra of a module, its involution and the unitary operators it defines.
