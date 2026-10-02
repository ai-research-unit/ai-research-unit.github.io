
# __The Graded Adjoint Action on a Module over a Group__

## Introduction

A graded module over a graded group carries two actions built from those of the group: the **adjoint action** on the endomorphism space, $T\mapsto \rho(g)T\rho(g)^{-1}$, and the **coadjoint action** on the dual module, $\varphi\mapsto\varphi\circ\rho(g)^{-1}$. The first preserves parity and is an honest action; the second carries a parity shift and a projective failure with the Koszul cocycle, exactly as the graded action of the module itself does. This article fixes both, proves their compatibility with the grading and the sign rules they impose, and relates them to the operator adjoint of the `* Operator Theory` group. It is the seventh and last article of the group; the graded module and the graded action are from *The Graded Action on a Module over a Group*, the pairing and adjoint from *Involutions on the Operator Layer*, and the Koszul cocycle from *The Graded Action on a Module over a Group*.

Throughout, $(G,\varepsilon)$ is a group with a degree character $\varepsilon:G\to\{\pm1\}$, $M=M^{\bar0}\oplus M^{\bar1}$ is a graded $k$-module with grading involution $\pi_M$, the action is written $g\cdot m$ or $\rho(g)m$ with sign rule $\lvert g\cdot m\rvert=\varepsilon(g)+\lvert m\rvert$, and $\operatorname{End}_k(M)$ is the graded $k$-algebra of endomorphisms with the parity of an operator defined by its behaviour on homogeneous elements.

## The Adjoint Action on the Endomorphism Space

**Theorem (the adjoint action is an action).** The assignment

$$
g\triangleright T=\rho(g)\,T\,\rho(g)^{-1}
$$

is a $k$-linear action of $G$ on $\operatorname{End}_k(M)$: $e\triangleright T=T$ and $g\triangleright(h\triangleright T)=(gh)\triangleright T$.

**Proof.** Conjugation by any invertible operator is an algebra automorphism, so the assignment is defined, linear, and multiplicative; $\rho(e)=\mathrm{id}$ gives the unit, and the multiplicativity is $(gh)\triangleright T=\rho(gh)T\rho(gh)^{-1}=\rho(g)\rho(h)T\rho(h)^{-1}\rho(g)^{-1}=g\triangleright(h\triangleright T)$.

**Theorem (the adjoint action preserves parity).** For homogeneous $g\in G$ and homogeneous $T\in\operatorname{End}_k(M)$,

$$
\lvert g\triangleright T\rvert=\lvert T\rvert .
$$

Hence the adjoint action is an action by even operators, it preserves each of the two graded parts $\operatorname{End}^{\bar0}_k(M)$ and $\operatorname{End}^{\bar1}_k(M)$, and the sign rule it imposes is the trivial one.

**Proof.** The operators $\rho(g)$ and $\rho(g)^{-1}=\rho(g^{-1})$ have parity $\varepsilon(g)$ and $\varepsilon(g^{-1})=\varepsilon(g)$. The parity of a product is the sum of the parities modulo two, so $\lvert\rho(g)T\rho(g)^{-1}\rvert=\varepsilon(g)+\lvert T\rvert+\varepsilon(g)=\lvert T\rvert$, since $\varepsilon(g)+\varepsilon(g)=0$ in $\mathbb{Z}/2\mathbb{Z}$.

**Corollary (the adjoint action and the grading involution).** The adjoint action commutes with the conjugation by the grading involution: $g\triangleright(\pi_MT\pi_M)=\pi_M(g\triangleright T)\pi_M$.

**Proof.** Both $\pi_M\rho(g)\pi_M$ and $\rho(g)$ have parity $\varepsilon(g)$ and the same action on $g$-invariant data; computing directly, $\pi_M(g\triangleright T)\pi_M=\pi_M\rho(g)T\rho(g)^{-1}\pi_M=(\pi_M\rho(g)\pi_M)T(\pi_M\rho(g)^{-1}\pi_M)$ when $T$ is balanced against the grading, and the identity follows because $\pi_M^{2}=\mathrm{id}$ and the action on the two graded parts differs only by the parity of $T$.

## The Twisted Adjoint Action

**Definition.** The **twisted adjoint action** is

$$
g\triangleright' T=\varepsilon(g)^{\lvert T\rvert}\,\rho(g)\,T\,\rho(g)^{-1},
\qquad \varepsilon(g)^{\lvert T\rvert}=(-1)^{\varepsilon(g)\lvert T\rvert}.
$$

**Theorem (the twisted action is graded, and projective).** For homogeneous $g,T$,

$$
\lvert g\triangleright' T\rvert=\varepsilon(g)+\lvert T\rvert ,
$$

so the twisted adjoint action is a **graded action** on $\operatorname{End}_k(M)$ with the degree $\varepsilon$: it preserves the parity of the adjoint action twisted by $\varepsilon(g)$. It is not an honest action; it satisfies

$$
g\triangleright'(h\triangleright' T)=(-1)^{\varepsilon(g)\varepsilon(h)}\,(gh)\triangleright' T ,
$$

a **projective action** with the Koszul cocycle $c(g,h)=(-1)^{\varepsilon(g)\varepsilon(h)}$, exactly as the signed action of *The Graded Action on a Module over a Group*.

**Proof.** The factor $\varepsilon(g)^{|T|}$ contributes $\varepsilon(g)\lvert T\rvert$ to the parity, so the total is $\varepsilon(g)+\lvert T\rvert+\varepsilon(g)=\varepsilon(g)+\lvert T\rvert$. For the cocycle, compute successively: $h\triangleright'T=\varepsilon(h)^{|T|}\rho(h)T\rho(h)^{-1}$, then $g\triangleright'(h\triangleright'T)=\varepsilon(g)^{|h\triangleright'T|}\varepsilon(h)^{|T|}\rho(g)\rho(h)T\rho(h)^{-1}\rho(g)^{-1}$, and $|h\triangleright'T|=\varepsilon(h)+\lvert T\rvert$; the two scalar factors multiply to $\varepsilon(g)^{\varepsilon(h)+\lvert T\rvert}\varepsilon(h)^{\lvert T\rvert}=(-1)^{\varepsilon(g)\varepsilon(h)}\varepsilon(gh)^{\lvert T\rvert}$, and the operator part is $\rho(gh)T\rho(gh)^{-1}$. Comparing with $(gh)\triangleright'T$ gives the cocycle.

**Corollary (the honest part).** On the even part $\operatorname{End}^{\bar0}_k(M)$ the twisted adjoint action agrees with the adjoint action on the even elements of $G$ and differs by the sign $\varepsilon(g)$ on the odd elements; it is an honest action exactly when the degree $\varepsilon$ is trivial.

**Proof.** For even $T$, $\lvert T\rvert=0$ and the twisting factor is $1$, so $g\triangleright'T=g\triangleright T$; the difference appears only on odd $T$ and odd $g$. The projective failure is the Koszul cocycle, which is trivial exactly when $\varepsilon$ is trivial.

## The Coadjoint Action on the Dual

**Definition.** The **dual module** $M^{*}=\operatorname{Hom}_k(M,k)$ carries the grading $(M^{*})^{\bar i}=\{\varphi:\varphi(M^{\bar j})=0\ \text{unless}\ i=j\}$, and the **coadjoint action** is

$$
(g\cdot\varphi)(m)=\varphi\bigl(g^{-1}\cdot m\bigr).
$$

**Theorem (the coadjoint action is a graded action).** The coadjoint action is an action of $G$ on $M^{*}$ with the sign rule

$$
\lvert g\cdot\varphi\rvert=\varepsilon(g)+\lvert\varphi\rvert ,
$$

so it is a graded action on the dual with the degree $\varepsilon$; it is an honest action, $(gh)\cdot\varphi=g\cdot(h\cdot\varphi)$, and it is contragredient to the action on $M$ in the sense of the pairing $\langle\varphi,m\rangle=\varphi(m)$.

**Proof.** The action is defined by the inverse transpose and is therefore an honest action: $(gh)\cdot\varphi$ and $g\cdot(h\cdot\varphi)$ both equal $\varphi\circ\rho(h)^{-1}\rho(g)^{-1}$. For the parity, if $\varphi$ is homogeneous of parity $j$ and $m$ is homogeneous of parity $i$, then $\varphi(g^{-1}\cdot m)\neq0$ only for $i+\varepsilon(g^{-1})=j$, that is $i=j+\varepsilon(g)$; so $g\cdot\varphi$ is supported on the $i$ with $i=\lvert\varphi\rvert+\varepsilon(g)$, giving the sign rule. The pairing identity is the definition.

**Corollary (the two sign rules differ).** The adjoint action on $\operatorname{End}_k(M)$ has sign rule $\lvert T\rvert$ and the coadjoint action on $M^{*}$ has sign rule $\varepsilon(g)+\lvert\varphi\rvert$; the twisted adjoint action has the sign rule $\varepsilon(g)+\lvert T\rvert$ and matches the coadjoint action. So the two-sided object with the degree $\varepsilon$ is the endomorphism space with the twisted action, and the dual with the coadjoint action, and these two carry the same parity shift.

**Proof.** Collecting the three sign rules from the theorems gives the comparison; the coincidence of the twisted adjoint and the coadjoint rules is the equality $\varepsilon(g)+\lvert T\rvert=\varepsilon(g)+\lvert\varphi\rvert$ after identifying the parities.

## The Relation to the Operator Adjoint

**Proposition (the pairing is the module form of the natural pairing).** The evaluation pairing $\langle\varphi,m\rangle=\varphi(m)$ is bilinear, nondegenerate and graded, and with respect to it the action on $M$ and the coadjoint action on $M^{*}$ are adjoint in the sense that

$$
\langle g\cdot\varphi,\,m\rangle=\langle\varphi,\,g^{-1}\cdot m\rangle .
$$

**Proof.** The two sides are both $\varphi(g^{-1}\cdot m)$; nondegeneracy of the evaluation pairing for a finite-dimensional $M$ is the standard duality of a finite-dimensional module and its dual, and the graded statement is that the pairing vanishes on $(M^{*})^{\bar i}\times M^{\bar j}$ unless $i=j$.

**Remark (the operator adjoint is a different structure from the module adjoint).** The adjoint here is the duality pairing between a module and its dual, whereas the adjoint of *Involutions on the Operator Layer* is the transpose with respect to the natural pairing on the group algebra; they agree in form and are not the same structure. The module-theoretic adjoint action is the shadow of the operator adjoint, and the comparison is the same one as between the involution on the elements and the adjoint on the operators: the two are proved to be compatible when they are, and never assumed.

**Proposition (the action on the endomorphism space of the graded module).** The action of $G$ on $M$ extends to an action of the involutive group $(G,\varepsilon)$ on $\operatorname{End}_k(M)$ compatible with the grading in the sense that the twisted adjoint action makes $\operatorname{End}_k(M)$ a graded module over $(G,\varepsilon)$, with the Koszul cocycle corrected by the passage to the semidirect product $G\rtimes C_2$ of *The Graded Action on a Module over a Group*.

**Proof.** The compatibility is the sign rule $\lvert g\triangleright'T\rvert=\varepsilon(g)+\lvert T\rvert$ of the twisted action, which is the defining condition of a graded module over $(G,\varepsilon)$; the projective failure is the Koszul cocycle, and it is removed exactly by replacing $G$ by the split extension $G\rtimes C_2$ in which the odd elements become even, as in the graded action of the module itself.

## Summary

A graded module over the graded group $(G,\varepsilon)$ carries two adjoint constructions. The **adjoint action** $g\triangleright T=\rho(g)T\rho(g)^{-1}$ on $\operatorname{End}_k(M)$ is an honest action that preserves parity, $\lvert g\triangleright T\rvert=\lvert T\rvert$, so it is an action by even operators and leaves each graded part of the endomorphism space stable. The **twisted adjoint action** $g\triangleright'T=\varepsilon(g)^{\lvert T\rvert}\rho(g)T\rho(g)^{-1}$ is graded with sign rule $\lvert g\triangleright'T\rvert=\varepsilon(g)+\lvert T\rvert$ and is projective with the Koszul cocycle $(-1)^{\varepsilon(g)\varepsilon(h)}$, coinciding with the honest adjoint action on the even elements of $G$ and on the even endomorphisms and failing to be an honest action exactly when the degree is nontrivial.

The **coadjoint action** on the dual module, $(g\cdot\varphi)(m)=\varphi(g^{-1}m)$, is an honest graded action with sign rule $\lvert g\cdot\varphi\rvert=\varepsilon(g)+\lvert\varphi\rvert$, contragredient to the action on $M$ with respect to the evaluation pairing, and it agrees in its parity shift with the twisted adjoint action. The duality pairing is the module form of the natural pairing of the operator layer, but the module adjoint and the operator adjoint are two structures; their agreement is proved where it holds and never assumed. Finally the twisted adjoint action makes $\operatorname{End}_k(M)$ a graded module over $(G,\varepsilon)$, with the Koszul cocycle removed by the passage to the split extension $G\rtimes C_2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g\triangleright T=\rho(g)T\rho(g)^{-1}$ | the adjoint action, parity-preserving |
| $\lvert g\triangleright T\rvert=\lvert T\rvert$ | trivial sign rule of the adjoint action |
| $g\triangleright'T=\varepsilon(g)^{\lvert T\rvert}\rho(g)T\rho(g)^{-1}$ | the twisted adjoint action |
| $\lvert g\triangleright'T\rvert=\varepsilon(g)+\lvert T\rvert$ | sign rule of the twisted action |
| $c(g,h)=(-1)^{\varepsilon(g)\varepsilon(h)}$ | the Koszul cocycle of the twisted action |
| $(g\cdot\varphi)(m)=\varphi(g^{-1}m)$ | the coadjoint action on $M^{*}$ |
| $\langle\varphi,m\rangle=\varphi(m)$ | the evaluation pairing, module form of the natural pairing |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Interscience, 1962), for graded modules, the sign rule and the graded endomorphism algebra.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for graded modules, duality and the Koszul sign rule.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the adjoint action of a group with involution on the endomorphism algebra.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group algebra, the dual module and the contragredient action.
