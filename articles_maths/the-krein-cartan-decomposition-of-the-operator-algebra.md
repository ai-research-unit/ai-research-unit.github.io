# __The Krein Cartan Decomposition of the Operator Algebra__

## Introduction

The general quaternionic sesquilinear form on $\mathbb{B}$ induces on the algebra of $\mathbb{C}$-linear operators of $\mathbb{B}$ — a copy of $M_4(\mathbb{C})$ — an adjoint, an involution, a Lie algebra and a symmetric space, and the whole of the indefinite operator theory of this category is written in those terms. This article sets up that structure: the **three adjoints** of the operator algebra (the transpose of the general quaternionic bilinear form, the Hermitian adjoint, the Krein adjoint), the **three involutions** they define and the three classical Lie algebras that are their fixed spaces — the complex orthogonal algebra, $\mathfrak{u}(4)$ and $\mathfrak{u}(1,3)$; the **Krein decomposition** $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ into $J$-skew and $J$-self-adjoint operators; the involution $T\mapsto(T^{\dagger})^{-1}$ of the group and the reason it is *not* a Cartan involution; and the Cartan involution of $U(1,3)$ itself, whose symmetric space is the complex hyperbolic space of *The Krein Level Sets and the Hyperbolic Structure*. The group is *The Krein Isometry Group and Its $J$-Contractions*; the individual operators are *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions*.

**Conventions.** $\mathbb{B}\cong\mathbb{C}^{4}$ with coefficient basis $e_0,e_1,e_2,e_3$; the general plain sesquilinear form has Gram matrix $\mathrm{I}_4$, the general quaternionic bilinear form $\mathrm{I}_4$ and the general quaternionic sesquilinear form $E=\mathrm{diag}(1,-1,-1,-1)$; $J={}^{\natural}$ with matrix $E$; the Krein adjoint of an operator $M$ is $M^{\dagger}=JM^{*}J$, where $M^{*}$ is the conjugate transpose; and $\mathfrak{g}=\mathrm{End}_{\mathbb{C}}(\mathbb{B})$ is the real Lie algebra of all $\mathbb{C}$-linear operators, of real dimension $32$.

## The Three Adjoints of the Operator Algebra

**Theorem (the three involutions).** On $\mathfrak{g}$ the three pairings of *The Four Pairings of the Biquaternion Algebra* define three adjoints,

$$
\langle M\tilde{P},\tilde{Q}\rangle=\langle\tilde{P},M^{\mathsf T}\tilde{Q}\rangle,
\qquad
\langle M\tilde{P},\tilde{Q}\rangle=\langle\tilde{P},M^{*}\tilde{Q}\rangle,
\qquad
\langle\tilde{Q},M\tilde{P}\rangle_{\natural*}=\langle M^{\dagger}\tilde{Q},\tilde{P}\rangle_{\natural*},
$$

namely the **transpose** $M^{\mathsf T}$, the **Hermitian adjoint** $M^{*}$ and the **Krein adjoint** $M^{\dagger}=JM^{*}J$; in the coefficient basis these are the transpose, the conjugate transpose and the conjugate transpose conjugated by $E$. Each gives an involution of $\mathfrak{g}$,

$$
\theta_{\mathsf T}(M)=-M^{\mathsf T},\qquad
\theta_{*}(M)=-M^{*},\qquad
\theta_{J}(M)=-M^{\dagger}=-JM^{*}J .
$$

**Proof.** The three adjoints exist because the three forms are non-degenerate with invertible Gram matrices $\mathrm{I}_4,\mathrm{I}_4,E$, and the formulas in the basis are the standard ones for a bilinear, a sesquilinear and an $E$-sesquilinear form. The maps are $\mathbb{R}$-linear involutions of $\mathfrak{g}$.

**Theorem (the three fixed algebras).** The fixed algebras of the three involutions are the classical Lie algebras

$$
\mathfrak{g}^{\theta_{\mathsf T}}=\{M:M^{\mathsf T}=-M\}=\mathfrak{so}_4(\mathbb{C}),
\qquad
\mathfrak{g}^{\theta_{*}}=\{M:M^{*}=-M\}=\mathfrak{u}(4),
$$
$$
\mathfrak{g}^{\theta_{J}}=\{M:M^{\dagger}=-M\}=\mathfrak{u}(1,3),
$$

of real dimensions $12$, $16$ and $16$; each is closed under the commutator bracket, and the three are the Lie algebras of the isometry groups $O_4(\mathbb{C})$, $U(4)$ and $U(1,3)$ of the three pairings.

**Proof.** The fixed conditions are the defining equations $\mathfrak{so}_n$, $\mathfrak{u}(n)$ and $\mathfrak{u}(p,q)$; closure under the bracket is the standard fact for the fixed space of an involution that is an automorphism of the bracket, which each is, because $M\mapsto-M^{\mathsf T}$, $M\mapsto-M^{*}$ and $M\mapsto-M^{\dagger}$ satisfy $(MN)^{\sigma}=M^{\sigma}N^{\sigma}$ up to the sign pattern of a Lie algebra involution.

## The Krein Decomposition

**Definition.** The **Krein-decomposition** of $\mathfrak{g}$ is the eigenspace decomposition of the involution $\theta_{J}$,

$$
\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p},
\qquad
\mathfrak{k}=\{M:M^{\dagger}=-M\}=\mathfrak{u}(1,3),
\qquad
\mathfrak{p}=\{M:M^{\dagger}=M\}=J\cdot\mathrm{Herm}_4 .
$$

**Theorem (the decomposition and the bracket pattern).** The decomposition is direct, $\dim_{\mathbb{R}}\mathfrak{k}=\dim_{\mathbb{R}}\mathfrak{p}=16$, the relations

$$
\langle\mathfrak{k},\mathfrak{k}\rangle_{\natural*}\subseteq\mathfrak{k},
\qquad
\langle\mathfrak{p},\mathfrak{k}\rangle_{\natural*}\subseteq\mathfrak{p},
\qquad
\langle\mathfrak{p},\mathfrak{p}\rangle_{\natural*}\subseteq\mathfrak{k},
\qquad
\{\mathfrak{p},\mathfrak{p}\}\subseteq\mathfrak{p}
$$

hold, with $\{\cdot,\cdot\}$ the anticommutator, so $\mathfrak{k}$ is a Lie subalgebra, $\mathfrak{p}$ is a Jordan subalgebra, and the pair $(\mathfrak{k},\mathfrak{p})$ is a Lie–Jordan pair attached to the general quaternionic sesquilinear form.

**Proof.** $\mathfrak{k}$ and $\mathfrak{p}$ are the $\mp1$-eigenspaces of an involution, so they are direct and of equal dimension $32/2=16$. Write $M^{\epsilon}$ for an element with $M^{\dagger}=\epsilon M$, $\epsilon=\pm1$, and use $(AB)^{\dagger}=B^{\dagger}A^{\dagger}$. For $M,N\in\mathfrak{k}$ one has $(MN)^{\dagger}=(-N)(-M)=NM$, so $[M,N]^{\dagger}=NM-MN=-[M,N]$ and $[M,N]\in\mathfrak{k}$. For $M\in\mathfrak{k}$ and $N\in\mathfrak{p}$ one has $(MN)^{\dagger}=\langle-M,-M\rangle_{\natural}=-NM$ and $(NM)^{\dagger}=(-M)N=-MN$, so $[M,N]^{\dagger}=(MN)^{\dagger}-(NM)^{\dagger}=MN-NM=[M,N]$ and $[M,N]\in\mathfrak{p}$. For $M,N\in\mathfrak{p}$ one has $(MN)^{\dagger}=NM$, so $[M,N]^{\dagger}=NM-MN=-[M,N]$ and $[M,N]\in\mathfrak{k}$. Finally $\{M,N\}^{\dagger}=NM+MN=\{M,N\}$ for $M,N\in\mathfrak{p}$.

**Remark (the $J$-skew algebra is $J$ times the unitary algebra).** As vector spaces

$$
\mathfrak{u}(1,3)=J\cdot\mathfrak{u}(4)=\{JM:M\in\mathfrak{u}(4)\},
$$

since $(JM)^{\dagger}=JM^{*}$ is in $\mathfrak{u}(1,3)$ exactly when $M$ is skew-Hermitian; the identification is not a Lie algebra isomorphism, because $J$ is not central.

## The Involution of the Group

**Definition.** On the group $GL(\mathbb{B})$ of invertible operators define

$$
\theta_{J}(T)=\bigl(T^{\dagger}\bigr)^{-1}.
$$

**Theorem (the fixed group is $U(1,3)$).** The map $\theta_{J}$ is an involution with fixed group exactly the Krein isometry group $U_{J}(\mathbb{B})\cong U(1,3)$; its differential at the identity is the involution $\theta_{J}(M)=-M^{\dagger}$ of $\mathfrak{g}$ and its fixed algebra is $\mathfrak{k}=\mathfrak{u}(1,3)$.

**Proof.** $\theta_{J}^{2}(T)=\bigl((T^{\dagger})^{-1}\bigr)^{\dagger}{}^{-1}=(T^{\dagger\dagger})^{-1}{}^{-1}=T$, using $(S^{-1})^{\dagger}=(S^{\dagger})^{-1}$; the fixed condition $\theta_{J}(T)=T$ is $T^{\dagger}T=\mathrm{id}$, the definition of $J$-unitarity, and the group is $U(1,3)$.

**Theorem (the involution is not Cartan).** The fixed group $U_{J}(\mathbb{B})\cong U(1,3)$ of $\theta_{J}$ is non-compact, so $\theta_{J}$ is not a Cartan involution of $GL(\mathbb{B})$: the fixed group of a Cartan involution is compact by definition.

**Proof.** $U(1,3)$ contains the boosts, which are unbounded (*The Krein Isometry Group and Its $J$-Contractions*).

## The Cartan Involution of $U(1,3)$

**Theorem (the Cartan involution).** The restriction of the definite involution

$$
\theta_{0}(T)=(T^{*})^{-1}
$$

to the Krein isometry group is a Cartan involution of $U(1,3)$; its fixed group is the maximal compact subgroup $U(1)\times U(3)$, and its differential $\theta_{0}(M)=-M^{*}$ splits

$$
\mathfrak{u}(1,3)=\mathfrak{k}_{0}\oplus\mathfrak{p}_{0},
\qquad
\mathfrak{k}_{0}=\mathfrak{u}(1)\oplus\mathfrak{u}(3),
\qquad
\dim_{\mathbb{R}}\mathfrak{k}_{0}=10,\quad \dim_{\mathbb{R}}\mathfrak{p}_{0}=6 .
$$

**Proof.** For $T\in U(1,3)$, that is $T^{*}ET=E$, the operator $T^{*}$ is again in $U(1,3)$ and $\theta_{0}$ preserves the group; its fixed elements are the isometries that are unitary for $\langle\cdot,\cdot\rangle$, i.e. $U(4)\cap U(1,3)=U(1)\times U(3)$. The differential is $-M^{*}$, whose fixed algebra on $\mathfrak{u}(1,3)$ is $\mathfrak{u}(1)\oplus\mathfrak{u}(3)$ of real dimension $1+9=10$, leaving $\mathfrak{p}_{0}$ of dimension $16-10=6$; the fixed group is compact, which is the definition of a Cartan involution.

**Corollary (the symmetric space).** The quotient

$$
U(1,3)\,/\,\bigl(U(1)\times U(3)\bigr)
$$

is a Riemannian symmetric space of real dimension $6$, and it is the complex hyperbolic space $\mathbb{CH}^{3}$ of *The Krein Level Sets and the Hyperbolic Structure*, realised as the space of maximal positive definite subspaces, that is the open unit ball of $\mathbb{C}^{3}$.

**Proof.** The quotient of a Lie group by a maximal compact subgroup is a symmetric space of non-compact type, of dimension $\dim\mathfrak{p}_{0}=6$; the identification with the space of positive lines and with the ball is the parametrisation of the maximal positive definite subspaces. The Cartan decomposition of the group is

$$
U(1,3)=\bigl(U(1)\times U(3)\bigr)\cdot\exp(\mathfrak{p}_{0}),
$$

the compact part followed by the hyperbolic part, whose exponentials are the boosts and their conjugates.

## The Trace Form and the Killing Form

**Theorem (the trace form).** The pairing $(M,N)\mapsto\operatorname{Tr}(MN)$ is a non-degenerate general plain bilinear form on $\mathfrak{g}$, invariant under the three adjoints up to conjugation; restricted to $\mathfrak{u}(1,3)$ the definite form $(M,N)\mapsto\operatorname{Re}\operatorname{Tr}(MN)$ has signature $(6,10)$ on the real vector space of dimension $16$, positive on $\mathfrak{p}_{0}$ and negative on $\mathfrak{k}_{0}$.

**Proof.** The trace form is non-degenerate on $M_4(\mathbb{C})$, and $\operatorname{Tr}(MN)=\operatorname{Tr}(NM)$ makes it invariant under the adjoint action. For $\mathfrak{u}(p,q)$ the trace form is proportional to the Killing form, whose signature is $(2pq,p^{2}+q^{2})$, which for $p=1,q=3$ is $(6,10)$; this is the same statement as the Cartan decomposition of the previous section.

**Theorem (the Jordan cone).** The $J$-self-adjoint part $\mathfrak{p}=J\cdot\mathrm{Herm}_4$ is a Jordan algebra under the anticommutator, and it contains the $J$-positive cone $\mathcal{P}_{J}=J\cdot\{S\ge0\}$ of *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* as its cone of squares.

**Proof.** The anticommutator of two $J$-self-adjoint operators is $J$-self-adjoint, as shown above, and the Jordan axiom follows from associativity of the product in $\mathfrak{g}$. The cone statement is the definition of $\mathcal{P}_{J}$.

## Worked Examples

**Three involutions of the identity-map operator.** $M=\mathrm{id}$: $M^{\mathsf T}=M^{*}=M^{\dagger}=\mathrm{id}$, and $\theta(\mathrm{id})=-\mathrm{id}$ for each of the three involutions.

**The fundamental symmetry.** $M=J$: $J$ is the matrix $E$, self-adjoint for all three adjoints, and $\theta_{J}(J)=-J$; so $J\in\mathfrak{p}$, the $J$-self-adjoint part.

**A $J$-skew element.** $M=JL$, where $L$ is any definite-skew operator; $M^{\dagger}=-M$, so $M\in\mathfrak{k}=\mathfrak{u}(1,3)$.

**A boost generator.** The derivative at $t=0$ of the boost $T_{t}$ of *The Krein Isometry Group and Its $J$-Contractions* is the operator $H$ with $H e_0=e_1$, $H e_1=e_0$, $H e_2=H e_3=0$; it is $J$-self-adjoint, $H^{\dagger}=H$, hence an element of $\mathfrak{p}_{0}$, the hyperbolic part, and its exponential is the boost.

**A compact generator.** $M=L_{ie_0}$: skew-Hermitian and $J$-skew, an element of $\mathfrak{k}_{0}=\mathfrak{u}(1)\oplus\mathfrak{u}(3)$.

## Summary

The algebra of $\mathbb{C}$-linear operators of $\mathbb{B}$ is $\mathfrak{g}=M_4(\mathbb{C})=GL_4(\mathbb{C})$, of real dimension $32$, and the three pairings of the algebra give its three adjoints: the transpose $M^{\mathsf T}$ for the general quaternionic bilinear form, the Hermitian adjoint $M^{*}$, and the Krein adjoint $M^{\dagger}=JM^{*}J$. The corresponding involutions $M\mapsto-M^{\sigma}$ have the fixed algebras $\mathfrak{so}_4(\mathbb{C})$, $\mathfrak{u}(4)$ and $\mathfrak{u}(1,3)$, of real dimensions $12$, $16$ and $16$. The Krein involution splits $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ into the $J$-skew operators $\mathfrak{k}=\mathfrak{u}(1,3)$ and the $J$-self-adjoint operators $\mathfrak{p}=J\cdot\mathrm{Herm}_4$, each of dimension $16$; $\mathfrak{k}$ is a Lie algebra, $\mathfrak{p}$ a Jordan algebra, and the bracket of $\mathfrak{k}$ with $\mathfrak{p}$ stays in $\mathfrak{p}$. On the group the involution $T\mapsto(T^{\dagger})^{-1}$ has fixed group the non-compact $U(1,3)$, so it is not a Cartan involution; the Cartan involution is the restriction of $T\mapsto(T^{*})^{-1}$, whose fixed group is the maximal compact $U(1)\times U(3)$, with $\dim\mathfrak{k}_{0}=10$ and $\dim\mathfrak{p}_{0}=6$, and whose symmetric space is the complex hyperbolic space $\mathbb{CH}^{3}$ of real dimension $6$. The trace form of $\mathfrak{u}(1,3)$ has signature $(6,10)$, positive on the hyperbolic part and negative on the compact part, and the $J$-positive cone sits inside the Jordan algebra $\mathfrak{p}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{g}=\mathrm{End}_{\mathbb{C}}(\mathbb{B})\cong M_4(\mathbb{C})$ | The operator algebra; real dimension $32$ |
| $M^{\mathsf T}$, $M^{*}$, $M^{\dagger}=JM^{*}J$ | The three adjoints |
| $\theta_{\mathsf T},\theta_{*},\theta_{J}$ | The three involutions $M\mapsto-M^{\sigma}$ |
| $\mathfrak{so}_4(\mathbb{C})$, $\mathfrak{u}(4)$, $\mathfrak{u}(1,3)$ | The three fixed algebras; dimensions $12$, $16$, $16$ |
| $\mathfrak{g}=\mathfrak{k}\oplus\mathfrak{p}$ | The Krein decomposition |
| $\mathfrak{k}=\mathfrak{u}(1,3)$, $\mathfrak{p}=J\cdot\mathrm{Herm}_4$ | The $J$-skew and $J$-self-adjoint parts |
| $\theta_{J}(T)=(T^{\dagger})^{-1}$ | The group involution; fixed group $U(1,3)$, non-compact |
| $\theta_{0}(T)=(T^{*})^{-1}$, $U(1)\times U(3)$ | The Cartan involution and its fixed group |
| $U(1,3)/(U(1)\times U(3))\cong\mathbb{CH}^{3}$ | The symmetric space of real dimension $6$ |
| $(6,10)$ | The signature of the trace form of $\mathfrak{u}(1,3)$ |

## Further Reading

- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the three adjoints and the isometry groups
- *The Krein Isometry Group and Its $J$-Contractions* (`articles_maths/the-krein-isometry-group-and-its-j-contractions.md`), for $U(1,3)$, its maximal compact part and the boosts
- *J-Self-Adjoint and J-Unitary Operators on the General Quaternionic Sesqualgebra of Biquaternions* (`articles_maths/j-self-adjoint-and-j-unitary-operators-on-the-general-quaternionic-sesqualgebra-of-biquaternions.md`), for the Krein adjoint of the algebra's families
- *Indefinite Positivity and the Krein Cone of the Biquaternion Algebra* (`articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.md`), for the $J$-positive cone inside the Jordan part
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the complex hyperbolic space as the space of positive lines
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for Cartan involutions, Cartan decompositions and symmetric spaces of non-compact type
