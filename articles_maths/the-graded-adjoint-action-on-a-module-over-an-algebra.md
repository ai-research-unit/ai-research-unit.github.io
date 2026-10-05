# __The Graded Adjoint Action on a Module over an Algebra__

## Introduction

On a graded module over a graded algebra the adjoint operation acquires a **sign**: passing an operator of degree $|S|$ past one of degree $|T|$ past the pairing costs the Koszul sign $(-1)^{|S||T|}$, and the adjoint of a product is

$$
(ST)^{*}=(-1)^{|S||T|}\,T^{*}S^{*},
$$

the **graded involution** of the operator algebra, ordinary on the even operators and signed on the odd ones. The graded adjoint and the **sign-free adjoint** $\dagger$ of the earlier entries of the group differ by the grade involution alone, $T^{*}=\alpha_M^{\lvert T\rvert}T^{\dagger}$, so the grading, the sign and the involution are three readings of one operation. The graded action $\rho : A \to \operatorname{End}_k(M)$, $a\mapsto\rho(a)$, carries a homogeneous element of the algebra to an operator of the same degree, and its adjoint is computed by the same sign rule. The **graded adjoint action** is the graded commutator $\mathrm{ad}_x(y)=xy-(-1)^{|x||y|}yx$, the inner derivation of the graded algebra; as an operator it reads $\mathrm{ad}_x=L_x-R_x\alpha^{|x|}$, the grade involution acting on the argument, and its adjoints are explicit: $\mathrm{ad}_x^{\dagger}=R_x-\alpha^{|x|}L_x$ for the sign-free pairing and $\mathrm{ad}_x^{*}=\alpha^{|x|}\mathrm{ad}_x^{\dagger}$ for the graded one, so that an even $x$ gives $-\mathrm{ad}_x$ for both, while an odd $x$ produces the mirrored one-sided operators $R_x-\alpha L_x$ and $\alpha R_x-L_x$, which are not again adjoint actions.

This article fixes the graded pairing on a graded module, computes the adjoint of a homogeneous operator and the Koszul sign rule, relates the graded adjoint to the graded involution $\alpha$ of the algebra and the module, records the adjoint of the action map, and treats the graded adjoint action with its degree and its two adjoints. It assumes *The Graded Action on a Module over an Algebra* for the graded module, the action map $\rho$ and the sign rule of the graded commutator, *The Operators on an Algebra* and *The Sandwich Operator on an Algebra* for $L_a$, $R_a$ and $T_{a,b}$, *The Commutator Operator* for the inner derivations, *Involutions of the Operator Algebra*, *The Adjoint in an Involutive Algebra* and *Unitary Operators of an Involutive Algebra* for the adjoint operation, the two pairings and the unitary operators, *The Adjoint of the Left Multiplication on an Algebra*, *The Signed Adjoint Sandwich on an Algebra* and *The Signed Adjoint of the Left Multiplication on an Algebra* for the one-sided and the signed adjoints, *Involutive Bilinear Algebras*, *Involutive Graded Algebras* and *The Self-Adjoint Part of an Algebra* for the involutions, the grading and the fixed parts, and *Superalgebras and Graded Structures* for the Koszul rule and the symmetric monoidal structure. The module case over a graded algebra is *The Graded Adjoint Action on a Module over a Graded Algebra* of the later category *Symmetric Bilinear Algebras*; the analytic case is Part II. This article stays inside Part I: no distance, norm, form with a norm, topology or limit.

Throughout, $k$ is a field of characteristic not two, $A$ is a finite-dimensional unital associative $k$-algebra with an involutive automorphism $\alpha$ and the induced grading $A=A^0\oplus A^1$ of *The Signed Sandwich on an Algebra*, and $\tau$ is a trace with nondegenerate product pairing on $A$. The graded module is $M=M^0\oplus M^1$ over $A$ in the sense of *The Graded Action on a Module over an Algebra*, the action map is $\rho(a)(m)=a\cdot m$, the **grade involution of the module** is the operator $\alpha_M(m)=(-1)^{|m|}m$, homogeneous elements carry the parity $|x|\in\{0,1\}$ and the sign $(-1)^{|x||y|}$ is the Koszul sign, and the pairing on $M$ is graded, supersymmetric and nondegenerate. The sign-free adjoint of the earlier entries is written $T^{\dagger}$, the graded adjoint $T^{*}$, the one-sided operators are $L_a$, $R_a$ on $A$, and $\mathrm{ad}_x(y)=xy-(-1)^{|x||y|}yx$.

## The Graded Pairing and the Koszul Adjoint

**Definition.** A pairing $\langle\cdot,\cdot\rangle : M \times M \to k$ on the graded module is **graded** when it is biadditive and homogeneous of degree zero, $\lvert\langle x,y\rangle\rvert=\lvert x\rvert+\lvert y\rvert$, so that it vanishes on a pair of opposite parity; it is **supersymmetric** when

$$
\langle y,x\rangle=(-1)^{\lvert x\rvert\lvert y\rvert}\langle x,y\rangle ,
$$

and **nondegenerate** when $\langle x,M\rangle=0$ and $\langle M,y\rangle=0$ force $x=0$ and $y=0$. A graded, supersymmetric, nondegenerate pairing is a **graded pairing of the category**.

**Definition.** Let $\langle\cdot,\cdot\rangle$ be a graded nondegenerate pairing on $M$ and let $T$ be a homogeneous operator of degree $\lvert T\rvert$. The **graded adjoint** of $T$ is the operator $T^{*}$ defined by

$$
\langle Tx,y\rangle=(-1)^{\lvert T\rvert\lvert x\rvert}\langle x,T^{*}y\rangle
$$

for homogeneous $x$ and extended by linearity; dropping the sign gives the **sign-free adjoint** $T^{\dagger}$ of the earlier entries of the group,

$$
\langle Tx,y\rangle=\langle x,T^{\dagger}y\rangle .
$$

**Theorem.** Both adjoints exist and are unique, they are homogeneous of the same degree, $\lvert T^{*}\rvert=\lvert T^{\dagger}\rvert=\lvert T\rvert$, and for homogeneous $S,T$

$$
(ST)^{*}=(-1)^{\lvert S\rvert\lvert T\rvert}\,T^{*}S^{*}, \qquad (ST)^{\dagger}=T^{\dagger}S^{\dagger}, \qquad (T^{*})^{*}=T, \qquad \mathrm{id}^{*}=\mathrm{id} .
$$

The graded adjoint is therefore an anti-automorphism of order two **up to the Koszul sign**, and the sign-free adjoint one of order two without a sign: the two rules differ exactly on a pair of odd operators and agree on everything else, which is the graded involution of the operator algebra.

*Proof.* Existence and uniqueness are those of *Involutions of the Operator Algebra* applied to each homogeneous degree: the functional $x\mapsto(-1)^{|T||x|}\langle Tx,y\rangle$ is linear and is represented by a unique $T^{*}y$, and the representing element is homogeneous of degree $|T|+|y|$ because the pairing has degree zero. For the sign rule, move $S$ and then $T$ across the pairing: $\langle STx,y\rangle=(-1)^{|S||Tx|}\langle Tx,S^{*}y\rangle=(-1)^{|S|(|T|+|x|)}(-1)^{|T||x|}\langle x,T^{*}S^{*}y\rangle=(-1)^{|S||T|}(-1)^{(|S|+|T|)|x|}\langle x,T^{*}S^{*}y\rangle$, which is the defining identity of $(-1)^{|S||T|}T^{*}S^{*}$; the sign-free rule is the same computation with both signs dropped; the order-two and the unit statements are the defining identity read twice and at the identity.

**Corollary.** On the even operators the Koszul sign is $1$ and the graded adjoint is the sign-free adjoint of *Involutions of the Operator Algebra*; on products of odd operators the sign survives, and the composite of two odd operators is adjointed with the sign $-1$. The **self-adjoint** operators satisfy $T^{*}=T$ and the **skew-adjoint** ones $T^{*}=-T$ on each degree, and the decomposition $T=\tfrac12(T+T^{*})+\tfrac12(T-T^{*})$ is the one of *The Self-Adjoint Part of an Algebra*, taken degree by degree.

*Proof.* The sign $(-1)^{|S||T|}$ is $1$ unless both operators are odd, which gives the first two statements; the decomposition is the splitting of a degree-zero operator into fixed and negated parts, and each homogeneous component is carried to itself because the adjoint preserves the degree.

## The Graded Involution and the Adjoint

**Definition.** The **grade involution of the module** is the operator

$$
\alpha_M(m)=(-1)^{\lvert m\rvert}m ;
$$

it is an operator of order two, it is self-adjoint for every graded pairing, and it is the module analogue of the grade involution $\alpha$ of the algebra.

**Theorem.** The graded adjoint and the sign-free adjoint differ by the grade involution alone,

$$
T^{*}=\alpha_M^{\lvert T\rvert}\,T^{\dagger},
$$

where $\alpha_M^{\lvert T\rvert}$ is the identity on the even operators and the grade involution applied to the values on the odd ones; consequently the two adjoints agree exactly on the even operators. The pairing twisted by the grade involution,

$$
\{x,y\}_\alpha=\langle x,\alpha_My\rangle ,
$$

is graded and supersymmetric, and the graded adjoint for the twisted pairing is the conjugate of the graded adjoint for the plain one,

$$
T^{*_\alpha}=\alpha_M\,T^{*}\,\alpha_M=c_{\alpha_M}(T^{*}),
$$

so the graded adjoint is moved by the grade involution when the pairing is.

*Proof.* For homogeneous $T$ the two defining identities read $(-1)^{|T||x|}\langle x,T^{*}y\rangle=\langle Tx,y\rangle=\langle x,T^{\dagger}y\rangle$ for every homogeneous $x$ and $y$; comparing the even $x$ and the odd $x$ separately, and using that each graded piece of $M$ is nondegenerate for a pairing of degree zero, the even parts of $T^{*}y$ and $T^{\dagger}y$ agree and their odd parts are opposite when $|T|=1$, while for $|T|=0$ the two identities coincide; that is $T^{*}=\alpha_M^{|T|}T^{\dagger}$ on homogeneous $y$, and hence on all of $M$. Supersymmetry of $\{\cdot,\cdot\}_\alpha$ is the computation $\{y,x\}_\alpha=\langle y,\alpha_Mx\rangle=(-1)^{|x||y|}\langle\alpha_Mx,y\rangle=(-1)^{|x||y|}\langle x,\alpha_My\rangle$, using the supersymmetry of $\langle\cdot,\cdot\rangle$ and the self-adjointness of $\alpha_M$; the conjugation identity is the dictionary $T^{*_\sigma}=c_{\sigma}(T^{*})$ of *The Adjoint in an Involutive Algebra* with the grade involution as the twist.

**Corollary.** The invariants of the grade involution — the even part of the module — are the elements on which $\alpha_M=\mathrm{id}$, and the twisted pairing restricts to the plain one there; the odd part is the negated part, on which the twisted pairing differs from the plain one by the sign $-1$.

*Proof.* The two eigenspaces of $\alpha_M$ are the graded pieces, and the twisted pairing is $\{x,y\}_\alpha=\langle x,y\rangle$ for even $y$ and $-\langle x,y\rangle$ for odd $y$.

## The Graded Action and its Adjoint

**Theorem.** The action map $\rho : A \to \operatorname{End}_k(M)$ is a homomorphism of unital algebras, it carries a homogeneous element to a homogeneous operator of the same degree, and

$$
\rho(a)\bigl(M^j\bigr) \subseteq M^{\,j+\lvert a\rvert} ;
$$

the adjoint of the action is computed by the Koszul rule, $(\rho(a)\rho(b))^{*}=(-1)^{\lvert a\rvert\lvert b\rvert}\rho(b)^{*}\rho(a)^{*}$, and $\rho(\alpha(a))=\alpha_M\rho(a)\alpha_M$ for the grade involutions.

*Proof.* The homomorphism property, the degree and the containment are *The Graded Action on a Module over an Algebra*; the Koszul rule is the theorem of the first section applied to the operators $\rho(a)$ and $\rho(b)$, whose degrees are $\lvert a\rvert$ and $\lvert b\rvert$; the last identity is the multiplicativity of $\alpha$ read through the action, $\alpha(a)\alpha_M(m)=\alpha_M(am)$, which is the degree rule $|am|=|a|+|m|$ in operator form.

**Theorem (the one-sided operators).** For homogeneous $x$, on the algebra read as a module over itself,

$$
L_x^{*}=\alpha^{\lvert x\rvert}R_x, \qquad R_x^{*}=\alpha^{\lvert x\rvert}L_x ,
$$

so the graded adjoint **preserves the side** and inserts the grade involution when the element is odd, while the sign-free adjoint exchanges the sides, $L_x^{\dagger}=R_x$ and $R_x^{\dagger}=L_x$, as in *The Adjoint of the Left Multiplication on an Algebra*; the two statements are the identity $T^{*}=\alpha_M^{|T|}T^{\dagger}$ at $T=L_x$ and $T=R_x$.

*Proof.* The sign-free identity is the one-line computation $\langle xu,v\rangle=\tau(xuv)=\tau(uvx)=\langle u,vx\rangle$ of the cited article, which gives $L_x^{\dagger}=R_x$, and the same computation on the other side gives $R_x^{\dagger}=L_x$; applying $T^{*}=\alpha_M^{|T|}T^{\dagger}$ to the two gives the graded statements.

**Corollary.** For an even element the graded and the sign-free adjoints coincide on the one-sided operators, $L_x^{*}=L_x^{\dagger}=R_x$; for an odd element the graded adjoint of $L_x$ is the right multiplication twisted by the grade involution, $\alpha R_x=L_{\alpha(x)}\alpha$. In particular $L_x$ is self-adjoint for the graded pairing exactly when $\lvert x\rvert$ is even and $x$ is central.

*Proof.* The coincidence is $T^{*}=\alpha_M^{|T|}T^{\dagger}$ at $|T|=0$; for odd $x$ the identity $\alpha R_x=L_{\alpha(x)}\alpha$ is the multiplicativity of $\alpha$; self-adjointness needs $L_x^{*}=L_x$, which by the theorem is $R_x=L_x$ for even $x$, that is centrality, and for odd $x$ would require the grade involution to fix every element of the algebra, which it does only when the grading is trivial.

## The Graded Adjoint Action

**Definition.** For $x \in A$ the **graded adjoint action** of $x$ is

$$
\mathrm{ad}_x(y)=xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx ,
$$

the graded commutator; for homogeneous $x$ it is a linear operator on $A$ and, through the action, on every graded module over $A$.

**Theorem.** For homogeneous $x$,

$$
\mathrm{ad}_x=L_x-R_x\alpha^{\lvert x\rvert},
$$

the grade involution acting on the **argument**; the operator is a graded derivation of degree $\lvert x\rvert$,

$$
\mathrm{ad}_x(yz)=\mathrm{ad}_x(y)z+(-1)^{\lvert x\rvert\lvert y\rvert}y\,\mathrm{ad}_x(z) ,
$$

it satisfies the graded antisymmetry and the graded Jacobi identity, so the graded commutator makes $A$ a graded Lie algebra and $\mathrm{ad}$ a representation of it with kernel the graded centre.

*Proof.* On homogeneous $y$ the second term is $(-1)^{|x||y|}yx=(R_x\alpha^{|x|})y$, which is the operator identity and then, by linearity, the general one; the graded Leibniz rule, the graded antisymmetry and the graded Jacobi identity are *The Graded Action on a Module over an Algebra* and *The Commutator Operator* with the Koszul signs inserted, and the kernel is the graded centre because $\mathrm{ad}_x=0$ says exactly that $x$ graded-commutes with every element.

**Theorem (the adjoints).** For homogeneous $x$, with respect to the sign-free and the graded pairings,

$$
\mathrm{ad}_x^{\dagger}=R_x-\alpha^{\lvert x\rvert}L_x, \qquad \mathrm{ad}_x^{*}=\alpha^{\lvert x\rvert}\mathrm{ad}_x^{\dagger} .
$$

Consequently, for **even** $x$ both adjoints are the negative of the operator itself,

$$
\mathrm{ad}_x^{\dagger}=\mathrm{ad}_x^{*}=-\mathrm{ad}_x ,
$$

so the graded adjoint action of an even element is skew-adjoint for both pairings; for **odd** $x$ the two adjoints are the mirrored one-sided operators

$$
\mathrm{ad}_x^{\dagger}=R_x-\alpha L_x, \qquad \mathrm{ad}_x^{*}=\alpha R_x-L_x ,
$$

which are **not** of the form $-\mathrm{ad}_z$: the sign of the graded commutator sits on the argument, and moving it through the adjoint moves it to the other side of the second term.

*Proof.* Adjoint the two terms of $\mathrm{ad}_x=L_x-R_x\alpha^{|x|}$ for the sign-free pairing: $L_x^{\dagger}=R_x$, and $(R_x\alpha^{|x|})^{\dagger}=(\alpha^{|x|})^{\dagger}R_x^{\dagger}=\alpha^{|x|}L_x$ because the grade involution is self-adjoint and of degree zero; this gives the first identity, and the second is $T^{*}=\alpha_M^{|T|}T^{\dagger}$ at $\lvert T\rvert=\lvert x\rvert$. For even $x$ the power of the grade involution is the identity, so both adjoints are $R_x-L_x=-\mathrm{ad}_x$. For odd $x$ the sign-free adjoint is $R_x-\alpha L_x$, whose second term carries the involution to the left of the argument, while $-\mathrm{ad}_z=-L_z+R_z\alpha$ carries it to the right; the two agree for no $z$ unless $\alpha$ fixes every element, which is the trivial grading.

**Corollary.** The graded adjoint action of an even element is the ordinary inner derivation $\mathrm{ad}_x=L_x-R_x$ of *The Commutator Operator*, and it is skew-adjoint for both the graded and the sign-free pairings; the adjoint action of an odd element is the graded derivation $L_x-R_x\alpha$ of *The Graded Action on a Module over an Algebra*, whose adjoints are the mirrored one-sided operators above. In particular the graded adjoint action of an even element is self-adjoint for no nonzero $x$.

*Proof.* Both statements are the theorem written for each parity; the even case is the inner derivation of the cited article, and self-adjointness would require $-\mathrm{ad}_x=\mathrm{ad}_x$, that is $2\,\mathrm{ad}_x=0$.

## Examples

**(a) The exterior algebra.** For $A=\Lambda(V)$ with the degree grading and the natural graded pairing, the graded adjoint action of a vector $v$ is $\mathrm{ad}_v(\omega)=v\omega-(-1)^{\lvert\omega\rvert}\omega v$, a graded derivation of degree one; its sign-free adjoint is $R_v-\alpha L_v$ and its graded adjoint is $\alpha R_v-L_v$, the two mirrored odd operators of the theorem.

**(b) The Clifford algebra.** With the Clifford product and the grading by degree, the adjoint action of a vector is the commutator on the even part and the anticommutator on the odd part; the even part of the algebra acts by skew-adjoint derivations for the plain pairing, and the odd part by the operators of the odd case above. The metric reading is Part II.

**(c) The matrix superalgebra.** $A=M_{p|q}$ with the transpose and the grading by blocks: the adjoint action is the graded commutator of matrices, the Koszul sign appears the moment two odd matrices are multiplied, and the adjoint of a product is $(ST)^{*}=(-1)^{|S||T|}T^{*}S^{*}$.

**(d) The trivial grading.** If $\lvert a\rvert=0$ for all $a$ the Koszul sign is $1$, the graded pairing is ordinary, the graded adjoint action is the plain commutator $\mathrm{ad}_x=L_x-R_x$, and the article reduces to *Involutions of the Operator Algebra*, *The Adjoint of the Left Multiplication on an Algebra* and *The Commutator Operator*.

## Summary

On a graded module over a graded algebra a graded nondegenerate supersymmetric pairing $\langle y,x\rangle=(-1)^{|x||y|}\langle x,y\rangle$ gives every homogeneous operator a homogeneous adjoint of the same degree with the Koszul sign rule $(ST)^{*}=(-1)^{|S||T|}T^{*}S^{*}$; dropping the sign gives the sign-free adjoint $\dagger$ with $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$, and the two are related by the grade involution alone, $T^{*}=\alpha_M^{|T|}T^{\dagger}$, so they agree exactly on the even operators and the adjoint operation is a graded involution, ordinary on the even operators and signed on the odd ones. The grade involution $\alpha_M$ of the module gives the twisted pairing $\{x,y\}_\alpha=\langle x,\alpha_My\rangle$, whose graded adjoint is the conjugate $T^{*_\alpha}=c_{\alpha_M}(T^{*})$. The graded action $\rho$ sends a homogeneous element to an operator of the same degree and is compatible with the grade involution, $\rho(\alpha(a))=\alpha_M\rho(a)\alpha_M$. The one-sided operators have $L_x^{*}=\alpha^{|x|}R_x$ and $R_x^{*}=\alpha^{|x|}L_x$, so the graded adjoint preserves the side up to the involution, against $L_x^{\dagger}=R_x$ for the sign-free one. The graded adjoint action reads $\mathrm{ad}_x=L_x-R_x\alpha^{|x|}$, a graded derivation of degree $|x|$; its sign-free adjoint is $R_x-\alpha^{|x|}L_x$ and its graded adjoint is $\alpha^{|x|}$ times that, so an even $x$ gives $-\mathrm{ad}_x$ for both, while an odd $x$ gives the mirrored one-sided operators $R_x-\alpha L_x$ and $\alpha R_x-L_x$. When the grading is trivial the Koszul sign is $1$, the graded adjoint is the sign-free adjoint, and the whole article returns the sign-free adjoint involution and the ordinary inner derivation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lvert a\rvert$ | parity of a homogeneous element |
| $(-1)^{\lvert a\rvert\lvert b\rvert}$ | Koszul sign |
| $\langle y,x\rangle=(-1)^{\lvert x\rvert\lvert y\rvert}\langle x,y\rangle$ | supersymmetric graded pairing |
| $\alpha$, $\alpha_M$ | grade involution of the algebra and of the module |
| $T^{*}$, $\langle Tx,y\rangle=(-1)^{\lvert T\rvert\lvert x\rvert}\langle x,T^{*}y\rangle$ | graded adjoint |
| $T^{\dagger}$, $\langle Tx,y\rangle=\langle x,T^{\dagger}y\rangle$ | sign-free adjoint of the earlier entries |
| $(ST)^{*}=(-1)^{\lvert S\rvert\lvert T\rvert}T^{*}S^{*}$, $(ST)^{\dagger}=T^{\dagger}S^{\dagger}$ | Koszul sign rule and its sign-free case |
| $T^{*}=\alpha_M^{\lvert T\rvert}T^{\dagger}$ | the two adjoints differ by the grade involution |
| $\{x,y\}_\alpha=\langle x,\alpha_My\rangle$, $T^{*_\alpha}=c_{\alpha_M}(T^{*})$ | the twisted pairing and its adjoint |
| $\rho$, $\rho(\alpha(a))=\alpha_M\rho(a)\alpha_M$ | the action map |
| $L_x^{*}=\alpha^{\lvert x\rvert}R_x$, $R_x^{*}=\alpha^{\lvert x\rvert}L_x$ | graded adjoints of the one-sided operators |
| $L_x^{\dagger}=R_x$ | sign-free adjoint of the left multiplication |
| $\mathrm{ad}_x(y)=xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx$ | the graded adjoint action |
| $\mathrm{ad}_x=L_x-R_x\alpha^{\lvert x\rvert}$ | the operator form |
| $\mathrm{ad}_x^{\dagger}=R_x-\alpha^{\lvert x\rvert}L_x$, $\mathrm{ad}_x^{*}=\alpha^{\lvert x\rvert}\mathrm{ad}_x^{\dagger}$ | the sign-free and the graded adjoints |
| even $x$: $\mathrm{ad}_x^{\dagger}=\mathrm{ad}_x^{*}=-\mathrm{ad}_x$ | the even case |
| odd $x$: $\mathrm{ad}_x^{\dagger}=R_x-\alpha L_x$, $\mathrm{ad}_x^{*}=\alpha R_x-L_x$ | the odd case |
| $\lvert a\rvert=0$ | trivial grading; the sign-free case |

## Further Reading

- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded algebras, graded modules and the Koszul sign rule.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the adjoint operation, the inner derivations and the trace form.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the adjoint under an involution and the involutive compatibility of the action.
- Matej Brešar, *Introduction to Noncommutative Algebra* (Springer, 2014), for the graded derivations, the graded adjoint action and the graded Lie structure.
