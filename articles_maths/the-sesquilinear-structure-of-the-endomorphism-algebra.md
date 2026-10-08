# __The Sesquilinear Structure of the Endomorphism Algebra__

## Introduction

The endomorphism algebra of a module with a form carries an involution, the adjoint taken against the form, and that involution is the datum that turns the associative algebra of the endomorphisms into a sesqualgebra. The adjoint of an endomorphism $T$ is the endomorphism $T^{\dagger}$ defined by $\Phi(Tu,v)=\Phi(u,T^{\dagger}v)$; it is additive in $T$, it reverses the product, $ (ST)^{\dagger}=T^{\dagger}S^{\dagger}$, it is of order two, and it is **conjugate-linear** in the scalar, $(\lambda T)^{\dagger}=\varsigma(\lambda)T^{\dagger}$, because the form carries the involution in its second slot. The pair of the composition and the adjoint is therefore a sesqualgebra over the base ring, and its derived product is

$$
S\star T=S\,T^{\dagger} ,
$$

the endomorphism version of the product $x\star y=xy^{*}$ of a sesqualgebra. The present article develops this structure: the involution and the conjugate-linear slot it carries, the derived product with its parities and its unit laws, the unitary endomorphisms and the inner $*$-automorphisms they induce, the involutions of the adjoint type that the algebra admits, and the three worked cases of the complex matrices, the quaternion matrices, and the biquaternion algebra, where the endomorphism algebra is that of the module over the field, of the module over the division ring, and of the algebra over its base field.

The subject belongs to the operator theory of the sesqualgebras, in the group *Operator Theory*. The adjoint operation itself, with its two rules and its parity obstruction, is *The Sesquilinear Adjoint Operator*; the form, its two slots and its sesqui-symmetry are *The Sesquilinear Product* and *Sesqualgebras*; the underlying associative algebra of the endomorphisms, its centre and its examples, is *The Endomorphism Algebra of a Module*; the unitary elements and the inner $*$-automorphisms of an algebra are *Units and the Unitary Elements*; the involutions of the adjoint type are *The Involutions of a Sesqualgebra*; and the operators whose adjoints the family here generalises are *The Adjoint of the Sesquilinear Sandwich* and *The Sesquilinear Sandwich Operator*.

**The boundaries.** The form on the module and its perfection are the standing hypothesis of *The Sesquilinear Adjoint Operator*; the adjoint in the bilinear layer, where the twist sits in the conjugation of the algebra rather than in the second slot of the form, is *The Adjoint in an Involutive Algebra*; the two-sided and one-sided operators of the sesqualgebra as an algebra over itself are *The Sesquilinear Sandwich Operator* and *The Left and Right Multiplication Operators of a Sesqualgebra*; and the unitary and antiunitary operators of an arbitrary sesqualgebra are *The Unitary Operators of a Sesqualgebra*. This article stays inside Part I: no distance, no limit, no completeness.

Throughout, $R$ is a commutative ring with $1$ without zero divisors, $\varsigma$ is an involution of $R$, and $M$ is a finitely generated free $R$-module of rank $n\ge 1$. The **form** is a map $\Phi:M\times M\to R$, additive in each variable, $R$-linear in the first and $\varsigma$-semilinear in the second,

$$
\Phi(\lambda u,v)=\lambda\,\Phi(u,v),\qquad \Phi(u,\lambda v)=\varsigma(\lambda)\,\Phi(u,v) ,
$$

sesqui-symmetric, $\Phi(v,u)=\varsigma\bigl(\Phi(u,v)\bigr)$, and **perfect**: the map $u\mapsto\Phi(u,\,\cdot\,)$ is a bijection of $M$ onto the dual of its conjugate. The endomorphism algebra is $E=\operatorname{End}_{R}(M)$, with the composition as its product and the identity $\mathrm{id}$ as its unit; the adjoint operation $T\mapsto T^{\dagger}$ is defined below, and juxtaposition denotes the composition. The centre of $E$ is $Z(E)$.

## The Adjoint Involution on the Endomorphism Algebra

### The Definition of the Adjoint

**Definition.** For $T\in E$ the **adjoint** of $T$ is the endomorphism $T^{\dagger}\in E$ defined by

$$
\Phi(Tu,v)=\Phi(u,T^{\dagger}v)\qquad\text{for all }u,v\in M .
$$

**Proposition (existence and uniqueness).** For every $T\in E$ the adjoint $T^{\dagger}$ exists and is unique.

**Proof.** Fix $v\in M$. The map $u\mapsto\Phi(Tu,v)$ is $R$-linear, because $T$ and the first slot of $\Phi$ are; and by the perfection of $\Phi$ the map $y\mapsto\Phi(\,\cdot\,,y)$ is an $R$-linear bijection of $M$ onto the dual of $M$. So there is a unique $y\in M$ with $\Phi(u,y)=\Phi(Tu,v)$ for all $u$, and $y$ is defined to be $T^{\dagger}v$. The assignment $v\mapsto T^{\dagger}v$ is additive and $R$-linear, because the right-hand side and the bijection are, so $T^{\dagger}$ is an endomorphism of $M$. $\square$

### The Involution

**Theorem (the adjoint is an anti-automorphism of order two).** For all $S,T\in E$ and all $\lambda\in R$,

$$
(ST)^{\dagger}=T^{\dagger}S^{\dagger},\qquad (T^{\dagger})^{\dagger}=T,\qquad (\lambda T)^{\dagger}=\varsigma(\lambda)\,T^{\dagger},\qquad \mathrm{id}^{\dagger}=\mathrm{id} .
$$

**Proof.** For the first, $\Phi(STu,v)=\Phi(Tu,S^{\dagger}v)=\Phi(u,T^{\dagger}S^{\dagger}v)$ shows that $T^{\dagger}S^{\dagger}$ satisfies the defining identity of $(ST)^{\dagger}$, and the adjoint is unique. For the second, read the defining identity with the roles of the two slots exchanged, $\Phi(Tv,u)=\Phi(v,T^{\dagger}u)$, and apply $\varsigma$; the sesqui-symmetry $\varsigma\bigl(\Phi(a,b)\bigr)=\Phi(b,a)$ turns the two sides into $\Phi(u,Tv)=\Phi(T^{\dagger}u,v)$, which is the defining identity of $(T^{\dagger})^{\dagger}$, so the two endomorphisms agree. For the third, $\Phi(\lambda Tu,v)=\lambda\,\Phi(Tu,v)=\lambda\,\Phi(u,T^{\dagger}v)$, and $\lambda\,\Phi(u,w)=\Phi\bigl(u,\varsigma(\lambda)w\bigr)$ by the second slot's rule, so $\varsigma(\lambda)T^{\dagger}$ is the adjoint of $\lambda T$. The last statement is $\Phi(u,v)=\Phi(u,\mathrm{id}\,v)$. $\square$

**Corollary (the involution, and the sesqualgebra).** The adjoint operation $T\mapsto T^{\dagger}$ is a $\varsigma$-semilinear anti-automorphism of order two of $E$; with it, $E$ is a sesqualgebra over $R$ with the base involution $\varsigma$, in the sense of *Sesqualgebras*. Its fixed elements are the **Hermitian endomorphisms**, $T^{\dagger}=T$, and the endomorphisms on which the adjoint acts as $-1$, $T^{\dagger}=-T$, are the **skew-Hermitian** ones.

**Proof.** The four laws of the theorem are exactly the defining laws of a $\varsigma$-semilinear involution on an associative algebra with unit. $\square$

### The Conjugate-Linear Slot

**Remark (where the twist sits).** The scalar law $(\lambda T)^{\dagger}=\varsigma(\lambda)T^{\dagger}$ is the trace of the form's second slot, and it is the whole difference between this involution and the conjugate of an ordinary bilinear adjoint. Read on the algebra, the involution is $\varsigma$-semilinear; read on the module, the adjoint value $T^{\dagger}$ is again an $R$-linear endomorphism, since $\Phi\bigl(u,T^{\dagger}(\lambda v)\bigr)=\Phi(Tu,\lambda v)=\varsigma(\lambda)\Phi(u,T^{\dagger}v)=\Phi(u,\lambda T^{\dagger}v)$ gives $T^{\dagger}(\lambda v)=\lambda T^{\dagger}v$, so it is the assignment $T\mapsto T^{\dagger}$ that carries the twist and not its values. The adjoint depends on the module together with the form, and not on the module alone. When $\varsigma=\mathrm{id}$ the twist disappears and the involution is $R$-linear, and then $E$ is an involutive algebra in the bilinear sense of *The Adjoint in an Involutive Algebra*.

## The Sesquilinear Structure

### The Derived Product

**Definition.** The **derived product** of the sesqualgebra $E$ is

$$
S\star T=S\,T^{\dagger} .
$$

**Theorem (the parities and the unit laws).** For all $R,S,T\in E$ and all $\lambda\in R$,

$$
(\lambda S)\star T=\lambda\,(S\star T),\qquad S\star(\lambda T)=\varsigma(\lambda)\,(S\star T) ,
$$

so $\star$ is a sesquilinear product in the sense of *The Sesquilinear Product*, $R$-linear in the first slot and $\varsigma$-semilinear in the second; and

$$
S\star\mathrm{id}=S,\qquad \mathrm{id}\star S=S^{\dagger},\qquad \mathrm{id}\star\mathrm{id}=\mathrm{id} ,
$$

so $\mathrm{id}$ is a right unit for $\star$, while the left unit law holds up to the adjoint and only $S^{\dagger}=S$ has $\mathrm{id}$ as a two-sided unit.

**Proof.** The first parity is the $R$-linearity of the composition in its first slot; the second is the scalar law of the adjoint, $S\star(\lambda T)=S\,\varsigma(\lambda)T^{\dagger}=\varsigma(\lambda)(S\star T)$. The unit laws are $\mathrm{id}^{\dagger}=\mathrm{id}$ and the definition of $\star$: $S\star\mathrm{id}=S\,\mathrm{id}^{\dagger}=S$ for every $S$, so $\mathrm{id}$ is a right unit, and $\mathrm{id}\star S=\mathrm{id}\,S^{\dagger}=S^{\dagger}$. $\square$

**Remark (the derived product is not the composition).** The product $\star$ is a new product on $E$, and it is not associative in general: $(S\star T)\star U=ST^{\dagger}U^{\dagger}$ while $S\star(T\star U)=S\,U\,T^{\dagger}$, and the two agree exactly when $T^{\dagger}U^{\dagger}=UT^{\dagger}$. This is the endomorphism form of the fact that the derived product of a sesqualgebra is the product of the algebra with the involution and not the product of the algebra; the associativity of the composition is the datum, and $\star$ need not inherit it. The associativity of $E$ and the two-sidedness of its unit are those of *The Endomorphism Algebra of a Module*, and they are read from the composition and not from $\star$.

### The Unitary Endomorphisms

**Definition.** An endomorphism $T$ is **unitary** when $T^{\dagger}=T^{-1}$, equivalently $T^{\dagger}T=TT^{\dagger}=\mathrm{id}$. The unitary endomorphisms form a group $U(E)$ under the composition, and the map $T\mapsto T^{\dagger}$ is its inversion.

**Theorem (the inner $*$-automorphisms).** Let $U$ be a unitary endomorphism. Then $\alpha_{U}(T)=U\,T\,U^{\dagger}$ is an $R$-linear automorphism of $E$ with $\alpha_{U}^{-1}=\alpha_{U^{\dagger}}$, the assignment $U\mapsto\alpha_{U}$ is a homomorphism $U(E)\to\operatorname{Aut}(E)$ whose kernel is the central unitary endomorphisms, and $\alpha_{U}$ is an $*$-automorphism, $\alpha_{U}(T^{\dagger})=\alpha_{U}(T)^{\dagger}$.

**Proof.** The multiplicativity of $\alpha_{U}$ is the associativity of the composition, and it is additive and $R$-linear; its inverse is $\alpha_{U^{\dagger}}$ because $\alpha_{U}\alpha_{U^{\dagger}}(T)=UU^{\dagger}TU^{\dagger}U=T$. The kernel is the set of unitary $U$ with $UTU^{\dagger}=T$ for all $T$, that is $UT=TU$ for all $T$, which is $Z(E)\cap U(E)$. For the $*$-law, $\alpha_{U}(T^{\dagger})=(UT^{\dagger}U^{\dagger})=(UTU^{\dagger})^{\dagger}=\alpha_{U}(T)^{\dagger}$. $\square$

**Remark.** The inner $*$-automorphism $\alpha_{U}$ is the endomorphism form of the inner $*$-automorphism $\alpha_{u}(x)=uxu^{*}$ of a unitary element, and in the matrix case it is the conjugation $T\mapsto UTU^{*}$ by a unitary matrix; the family is *Units and the Unitary Elements* read on the operators, and its kernel is the centre, exactly as there.

## The Involutions of the Endomorphism Algebra

**Theorem (the adjoint-type involutions).** Let $U$ be a unitary endomorphism and let

$$
\sigma_{U}(T)=U\,T^{\dagger}\,U^{\dagger} .
$$

Then $\sigma_{U}$ is a $\varsigma$-semilinear map of $E$ of order two up to an inner $*$-automorphism,

$$
\sigma_{U}^{2}=\alpha_{U^{2}} ,
$$

where $\alpha_{U^{2}}(T)=U^{2}\,T\,(U^{2})^{\dagger}$. Consequently $\sigma_{U}$ is an involution of $E$ exactly when $U^{2}$ is central, $\sigma_{U}\in\operatorname{Inv}(E)\iff U^{2}\in Z(E)$; and for every unitary $U$ one has $\sigma_{U}=\alpha_{U}\circ{}^{\dagger}$, so the family is the coset of the adjoint under the inner $*$-automorphisms.

**Proof.** The semilinearity is that of the adjoint and the $R$-linearity of $\alpha_{U}$. For the square, $\sigma_{U}^{2}(T)=U\bigl(UT^{\dagger}U^{\dagger}\bigr)^{\dagger}U^{\dagger}=U\,U\,T\,U^{\dagger}\,U^{\dagger}=U^{2}\,T\,(U^{2})^{\dagger}=\alpha_{U^{2}}(T)$. Hence $\sigma_{U}^{2}=\mathrm{id}$ exactly when $U^{2}T=T(U^{2})^{\dagger}$ for all $T$; with $U$ unitary, $(U^{2})^{\dagger}=(U^{2})^{-1}$, and $U^{2}T\,(U^{2})^{-1}=T$ for all $T$ is $U^{2}\in Z(E)$. The last statement is $\alpha_{U}(T^{\dagger})=UT^{\dagger}U^{\dagger}$. $\square$

**Corollary (the adjacent involution).** The adjoint itself is the member $U=\mathrm{id}$ of the family, $\sigma_{\mathrm{id}}={}^{\dagger}$; the inner $*$-automorphisms $\alpha_{U}$ are the automorphisms of the family and not involutions, save for the classes of order at most two in $U(E)/Z(E)$; and the family is closed under conjugation, $\alpha_{V}\sigma_{U}\alpha_{V}^{-1}=\sigma_{VUV^{\dagger}}$.

**Proof.** $\sigma_{\mathrm{id}}(T)=T^{\dagger}$; an inner $*$-automorphism is an involution exactly when $U^{2}$ is central, by the same computation read without the adjoint; and $\alpha_{V}\sigma_{U}\alpha_{V}^{-1}(T)=VU V^{\dagger}\,T\,(VU V^{\dagger})^{\dagger}$, since $\alpha_{V}^{-1}=\alpha_{V^{\dagger}}$, which is $\sigma_{VUV^{\dagger}}$. $\square$

**Remark (the family compares with the elements).** The involutions are the operator form of the involutions $\sigma_{u}(x)=ux^{*}u^{*}$ of a unitary element of a sesqualgebra, and the criterion is the same, $u^{2}\in Z(A)$ there and $U^{2}\in Z(E)$ here. Both families are the orbit of the adjoint under the group of inner $*$-automorphisms, read on $E$ in the first case and on the algebra $A$ in the second.

## Worked Cases

### The Complex Matrices

Let $R=\mathbb{C}$ with $\varsigma$ the conjugation, $M=\mathbb{C}^{n}$ with the form $\Phi(u,v)=\sum_{i}u_{i}\overline{v_{i}}$, and $E=\operatorname{End}_{\mathbb{C}}(\mathbb{C}^{n})=M_{n}(\mathbb{C})$ with the composition of matrices. The form is perfect and sesqui-symmetric, and the adjoint defined by $\Phi(Tu,v)=\Phi(u,T^{\dagger}v)$ is the **conjugate transpose**, $T^{\dagger}=T^{*}$, because $\Phi(Tu,v)=(Tu)^{T}\overline{v}=u^{T}T^{T}\overline{v}$ while $\Phi(u,T^{*}v)=u^{T}\overline{T^{*}v}=u^{T}\overline{T^{*}}\,\overline{v}$ and $\overline{T^{*}}=T^{T}$. So the scalar law reads $(\lambda T)^{\dagger}=\overline{\lambda}\,T^{*}$: the involution on $M_{n}(\mathbb{C})$ is the conjugate transpose, the endomorphism algebra is the sesqualgebra $M_{n}(\mathbb{C})$ of *Matrix Sesqualgebras*, its derived product is $S\star T=ST^{*}$, and its adjoint-type involutions are $\sigma_{U}(T)=UT^{*}U^{*}$ for a unitary matrix $U$, an involution exactly when $U^{2}$ is a scalar matrix.

### The Quaternion Matrices

Let $\mathbb{H}$ be the division ring of the quaternions with its conjugation $\varsigma_{\mathbb{H}}$, and let the base be $R=\mathbb{R}$ with the trivial involution $\varsigma=\mathrm{id}$. The module is $\mathbb{H}^{n}$ read as a right $\mathbb{H}$-module, and the form is the $\mathbb{H}$-valued **quaternionic Hermitian form**

$$
\Phi(u,v)=\sum_{i}\overline{u_{i}}\,v_{i} ,
$$

conjugate-linear in its first slot for $\varsigma_{\mathbb{H}}$ and $\mathbb{H}$-linear in its second, with $\Phi(v,u)=\overline{\Phi(u,v)}$. The form takes its values in $\mathbb{H}$ and not in the base ring, so this case sits outside the commutative framework of the article; it is the mirror of the convention used above, and over the noncommutative coefficients the mirror is forced: with the linearity in the first slot the two sides of the defining identity differ by the commutators of the entries of $T$ with the coordinates, whereas with the conjugate-linear first slot the identity holds term by term. The endomorphism algebra is $E=\operatorname{End}_{\mathbb{H}}(\mathbb{H}^{n})=M_{n}(\mathbb{H})$, and the adjoint is the **conjugate transpose**

$$
T^{\dagger}=\overline{T}^{T} .
$$

The base involution is trivial, $\varsigma=\mathrm{id}$, so the scalar law is $(\lambda T)^{\dagger}=\lambda\,T^{\dagger}$ for real $\lambda$ and the involution on $M_{n}(\mathbb{H})$ is $\mathbb{R}$-linear: this is the bilinear degeneration, in which the conjugate-linear slot of the complex case is carried by the coefficient conjugation of the form and not by the base. The unitary endomorphisms are those with $\overline{T}^{T}=T^{-1}$; and since $\varsigma=\mathrm{id}$ the two classes of *The Unitary Operators of a Sesqualgebra* coincide, the unitary and the antiunitary operators being the same $\mathbb{R}$-linear maps, so they do not form two separate families here. The twist of the case sits in the coefficient conjugation of the form and not in the base involution, and the form is Hermitian for that conjugation rather than $\varsigma$-symmetric for the base.

### The Biquaternion Algebra

Let $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}$ be the biquaternion algebra, a $\mathbb{C}$-algebra of complex rank four generated by $1,i,j,k$ with $i^{2}=j^{2}=k^{2}=-1$ and $ij=k$. With $R=\mathbb{C}$, $\varsigma$ the conjugation and the module $M=\mathbb{B}$ read over $\mathbb{C}$, let $*$ be the antilinear conjugation of $\mathbb{B}$, the one that negates $i,j,k$, and let $\tau$ be the trace functional with $\tau(\xi^{*})=\varsigma\bigl(\tau(\xi)\bigr)$, as in *The Sesquilinear Adjoint Operator*; then $\Phi(\xi,\eta)=\tau(\xi\eta^{*})$ is a perfect sesquilinear form, and the adjoint against it makes $E=\operatorname{End}_{\mathbb{C}}(\mathbb{B})$ a sesqualgebra over $\mathbb{C}$. The Hermitian form of *The Hermitian Form on the Biquaternion Algebra* is this same pairing with the two slots exchanged, conjugate-linear in the first rather than in the second; the exchange leaves the adjoint unchanged, both forms giving the conjugate transpose. The algebra $\mathbb{B}$ is isomorphic to the complex matrices $M_{2}(\mathbb{C})$, so the endomorphism algebra is the matrix algebra over the coordinate space of $\mathbb{B}$, and by *Biquaternions as a Vector Space over $\mathbb{C}$* one has

$$
\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_{4}(\mathbb{C}) ,
$$

the complex matrices of order four. The sesquilinear structure of the case is therefore that of $M_{4}(\mathbb{C})$ with the conjugate transpose, the case $n=4$ of the complex matrices above, read on the coordinates of the biquaternion algebra; the two products $ST$ and $ST^{*}$ of that matrix algebra are the two products by which the biquaternions are read, and the adjoint-type involutions $\sigma_{U}$ are indexed by the unitary matrices of order four, modulo the scalars.

## Summary

The adjoint of an endomorphism of a module with a perfect sesquilinear form is defined by $\Phi(Tu,v)=\Phi(u,T^{\dagger}v)$; it exists and is unique, and it is a $\varsigma$-semilinear anti-automorphism of order two of the endomorphism algebra,

$$
(ST)^{\dagger}=T^{\dagger}S^{\dagger},\qquad (T^{\dagger})^{\dagger}=T,\qquad (\lambda T)^{\dagger}=\varsigma(\lambda)\,T^{\dagger} .
$$

The scalar law is the conjugate-linear slot, and it is what makes the endomorphism algebra a sesqualgebra over the base ring rather than an involutive algebra; it collapses to the linear law exactly when $\varsigma=\mathrm{id}$.

With its adjoint the algebra carries the derived product $S\star T=ST^{\dagger}$, which is $R$-linear in the first slot and $\varsigma$-semilinear in the second, has $\mathrm{id}$ as a right unit, and is not associative in general; the unitary endomorphisms $T^{\dagger}=T^{-1}$ form a group, they induce the inner $*$-automorphisms $\alpha_{U}(T)=UTU^{\dagger}$, and they index the adjoint-type involutions $\sigma_{U}(T)=UT^{\dagger}U^{\dagger}$, which satisfy $\sigma_{U}^{2}=\alpha_{U^{2}}$ and are involutions exactly for the unitary $U$ with $U^{2}$ central; the adjoint is the case $U=\mathrm{id}$.

The worked cases are the complex matrices, where the adjoint is the conjugate transpose and the derived product is $S\star T=ST^{*}$; the quaternion matrices, where the base involution is trivial and the twist of the coefficient form leaves the involution $R$-linear; and the biquaternion algebra, where the endomorphism algebra is $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_{4}(\mathbb{C})$ and the structure is the case $n=4$ of the complex matrices.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Phi(u,v)$ | the perfect sesquilinear form, $R$-linear in $u$, $\varsigma$-semilinear in $v$ |
| $E=\operatorname{End}_{R}(M)$ | the endomorphism algebra of the module |
| $T^{\dagger}$ | the adjoint, defined by $\Phi(Tu,v)=\Phi(u,T^{\dagger}v)$ |
| $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$, $(T^{\dagger})^{\dagger}=T$ | the anti-automorphism law and the order two law |
| $(\lambda T)^{\dagger}=\varsigma(\lambda)T^{\dagger}$ | the conjugate-linear slot |
| $S\star T=ST^{\dagger}$ | the derived product |
| $U(E)$ | the unitary endomorphisms, $T^{\dagger}=T^{-1}$ |
| $\alpha_{U}(T)=UTU^{\dagger}$ | the inner $*$-automorphism of a unitary $U$ |
| $\sigma_{U}(T)=UT^{\dagger}U^{\dagger}$, $\sigma_{U}^{2}=\alpha_{U^{2}}$ | the adjoint-type involutions |
| $T^{\dagger}=T$ / $T^{\dagger}=-T$ | the Hermitian / skew-Hermitian endomorphisms |
| $M_{n}(\mathbb{C})$ | the worked case of the complex matrices, $T^{\dagger}=T^{*}$ |
| $M_{n}(\mathbb{H})$ | the quaternion case, $\varsigma=\mathrm{id}$, $R$-linear involution, $T^{\dagger}=\overline{T}^{T}$ |
| $\operatorname{End}_{\mathbb{C}}(\mathbb{B})\cong M_{4}(\mathbb{C})$ | the biquaternion case |
| $\tau$, $\varsigma(\tau(\xi))=\tau(\xi^{*})$ | the trace functional in the biquaternion case |

## Further Reading

- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the involutions of a ring, the Hermitian and skew-Hermitian elements and the adjoint of an endomorphism against a form.
- Irving Kaplansky, *Linear Algebra and Geometry: A Second Course* (Allyn and Bacon, 1969), for the sesquilinear and Hermitian forms over fields and division rings, the adjoint and the unitary group of a form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involution of the endomorphism algebra of a module with a form and the adjoint algebras of the classical groups.
- Sterling K. Berberian, *Baer $\ast$-Rings* (Springer, 1972), for the conjugate-linear slot of the adjoint and the two rules for the adjoint of a linear and of a conjugate-linear operator.
- The companion articles of this series: *The Sesquilinear Adjoint Operator*, *The Sesquilinear Product*, *The Endomorphism Algebra of a Module*, *Units and the Unitary Elements*, *The Involutions of a Sesqualgebra*, *The Unitary Operators of a Sesqualgebra*, *The Adjoint of the Sesquilinear Sandwich* and *The Sesquilinear Sandwich Operator*.
